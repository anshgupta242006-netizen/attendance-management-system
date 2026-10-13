
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openrouter/free"


def interpret_instruction(user_instruction):
    """Convert a natural-language request into a JSON command."""

    if not API_KEY:
        return {"error": "OPENROUTER_API_KEY is missing from your .env file."}

    system_prompt = """
You are an assistant for a student attendance management system.

Convert the user's instruction into exactly one JSON object.
Do not calculate attendance yourself. Python will do calculations.

Supported actions:
1. get_student: requires roll_no
2. get_all_attendance: requires no other fields
3. get_class_average: requires no other fields
4. update_attendance: requires roll_no, day, and status

For update_attendance, status must be Present, Absent, or Unrecorded.
Use Unrecorded when the user asks to remove or delete a day's attendance.

Rules:
- Never invent a roll number or day.
- If required information is missing or unclear, use action "clarify".
- Return JSON only, with no Markdown.

JSON formats:
{"action":"get_student","roll_no":"101"}
{"action":"get_all_attendance"}
{"action":"get_class_average"}
{"action":"update_attendance","roll_no":"102","day":"Day 3","status":"Present"}
{"action":"clarify","question":"Which student's roll number do you mean?"}
"""

    try:
        response = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_instruction}
                ],
                "max_tokens": 600,
                "temperature": 0
            },
            timeout=60
        )

        response.raise_for_status()
        result = response.json()
        content = result["choices"][0]["message"]["content"]

        if not content:
            return {"error": "The AI returned an empty response. Please try again."}

        command = json.loads(content)

        if not isinstance(command, dict) or not isinstance(
            command.get("action"), str
        ):
            return {"error": "The AI response was not a valid command object."}

        return command

    except requests.RequestException as error:
        return {"error": f"API request failed: {error}"}
    except (ValueError, KeyError, IndexError, TypeError):
        return {"error": "Could not read the AI response as valid JSON."}
