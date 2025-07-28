# import requests
# import json

# from embedder import retrieve_similar_examples


# # Get the instructor's prompt
# instructor_prompt = input("What are your assignment specs?\n")

# # Use this to convert the instructor's input into a full prompt
# def generate_prompt(instructor_prompt):
#     example = retrieve_similar_examples(instructor_prompt, 1)
#     solution = example["solution"]
#     test_code = example["test_code"]

#     prompt = (
#         f"You are given an instructor's assignment spec. "
#         f"Below is a similar example with its solution and corresponding test code. "
#         f"Use the example to generate Python unittests for the new spec.\n\n"
#         f"---\n"
#         f"🔁 Example Spec:\n{example['id']}\n"
#         f"💡 Example Solution:\n{solution}\n"
#         f"✅ Example Test Code:\n{test_code}\n"
#         f"---\n"
#         f"🆕 New Instructor Spec:\n{instructor_prompt}\n"
#         f"🧪 Generate unittest code for the new spec."
#     )

#     print("PROMPT HERE: ", prompt)
#     # return TypeError
#     return f"Generate Python unittests based on the following instructor specs:\n{instructor_prompt}"

# # Construct the actual prompt for the model
# prompt = generate_prompt(instructor_prompt)

# # Send the prompt to DeepSeek running on localhost
# response = requests.post(
#     "http://localhost:11434/api/generate",
#     headers={"Content-Type": "application/json"},
#     data=json.dumps({
#         "model": "deepseek-coder",
#         "prompt": prompt,
#         "stream": False
#     })
# )

# # Output the result
# result = response.json()
# print("\n🧪 Generated Test Code:\n")
# print(result["response"])


import requests
import json
from embedder import retrieve_similar_examples

# Get the instructor's prompt
instructor_prompt = input("What are your assignment specs?\n")

# Generate Windsurf prompt using RAG example
def generate_prompt(instructor_prompt):
    example = retrieve_similar_examples(instructor_prompt, 1)
    solution = example["solution"]
    test_code = example["test_code"]

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

    print("PROMPT HERE:\n", prompt)
    return prompt

# Construct the actual prompt
prompt = generate_prompt(instructor_prompt)

# Send the prompt to Windsurf AI
response = requests.post(
    "http://localhost:11434/api/generate",
    headers={"Content-Type": "application/json"},
    data=json.dumps({
        "model": "mistral:instruct",
        "prompt": prompt,
        "stream": False
    })
)

# Output the result
result = response.json()
print("\n🧪 Generated Test Code:\n")
print(result["response"])