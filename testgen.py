

from flask import Flask, request, jsonify
import requests
import json
from embedder import retrieve_similar_examples  # Make sure this exists
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/generate-test', methods=['POST'])
def generate_test():
    data = request.json
    instructor_prompt = data.get("prompt", "")
    
    if not instructor_prompt:
        return jsonify({"error": "Missing prompt"}), 400

    # Get RAG-based similar example
    example = retrieve_similar_examples(instructor_prompt, 1)
    solution = example["solution"]
    test_code = example["test_code"]

    # Format the Windsurf prompt
    prompt = (
        f"You are given an instructor's assignment spec. "
        f"Below is a similar example with its solution and corresponding test code. "
        f"Use the example to generate Python unittests for the new spec.\n\n"
        f"---\n"
        f"🔁 Example Spec:\n{example['id']}\n"
        f"💡 Example Solution:\n{solution}\n"
        f"✅ Example Test Code:\n{test_code}\n"
        f"---\n"
        f"🆕 New Instructor Spec:\n{instructor_prompt}\n"
        f"🧪 Generate unittest code for the new spec."
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        headers={"Content-Type": "application/json"},
        data=json.dumps({
            "model": "mistral:instruct",
            "prompt": prompt,
            "stream": False
        })
    )

    # result = response.json()
    # return jsonify({"response": result["response"]})

    print("🧠 Ollama raw response:", response.status_code, response.text)

    # Defensive check
    try:
        result = response.json()
        return jsonify({"response": result.get("response", "⚠️ No response field in Ollama output")})
    except Exception as e:
        print("❌ Failed to parse Ollama output:", e)
        return jsonify({"error": "Failed to get response from model"}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
