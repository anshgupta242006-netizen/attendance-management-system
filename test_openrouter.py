
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("ERROR: API key not found in .env")
    raise SystemExit(1)

print("API key loaded successfully.")

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "openrouter/free",
    "messages": [
        {
            "role": "user",
            "content": (
                'Return only this JSON: '
                '{"project":"Attendance Management System",'
                '"status":"connected"}'
            )
        }
    ],
    "temperature": 0,
    "max_tokens": 600,
    }

try:
    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=60
    )

    print("HTTP status:", response.status_code)

    if response.status_code != 200:
        print("Request failed:", response.text[:1000])
        raise SystemExit(1)

    data = response.json()

    print("\nFull model response details:")
    print(json.dumps(data, indent=2)[:5000])

    choices = data.get("choices", [])

    if choices:
        message = choices[0].get("message", {})
        content = message.get("content")

        if content:
            print("\nSUCCESS: Model generated a response.")
            print("Model:", data.get("model"))
            print("Content:", content)
        else:
            print("\nResponse received, but message content is empty.")
            print("Check the full response details above.")
    else:
        print("\nNo model choices returned.")

except requests.RequestException as error:
    print("Connection error:", error)
