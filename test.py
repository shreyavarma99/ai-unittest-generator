import requests

response = requests.post(
    "http://localhost:5001/generate-test",
    json={"prompt": "Write a Python function to check if a number is prime."}
)

# Print status and raw response
print("Status code:", response.status_code)
print("Raw response:", response.text)

# Try to decode JSON only if it's valid
try:
    print("JSON:", response.json())
except requests.exceptions.JSONDecodeError:
    print("❌ Response was not valid JSON.")
