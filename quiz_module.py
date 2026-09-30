"""Quiz generation (Gemini) -> list of 3 MCQs as JSON."""
import json
import re
from gemini_client import ask_gemini


def clean_json_block(text: str) -> str:
    """Remove Markdown code fences such as ```json ... ``` around a JSON reply."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def generate_quiz(passage: str):
    prompt = (
        "Create exactly 3 multiple-choice questions from the topic or passage below. "
        "Each question must have exactly 4 plausible options. "
        "Reply ONLY with valid JSON, no extra text, in this format:\n"
        '[{"question": "...", "options": ["A", "B", "C", "D"], "answer": "<must equal one option exactly>"}]\n\n'
        f"Topic or passage:\n{passage}"
    )
    try:
        raw = ask_gemini(prompt)
        quiz = json.loads(clean_json_block(raw))
        if not isinstance(quiz, list) or not quiz:
            raise ValueError("Model did not return a list of questions.")
        return quiz
    except json.JSONDecodeError as e:
        return {"error": f"Could not parse quiz JSON: {e}"}
    except Exception as e:
        return {"error": str(e)}
