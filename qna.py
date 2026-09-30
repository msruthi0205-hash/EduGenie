"""Question answering (Gemini)."""
from gemini_client import ask_gemini


def answer_question(question: str) -> str:
    prompt = (
        "You are EduGenie, a helpful tutor. Answer the student's question "
        "accurately and concisely (max 5 sentences).\n\n"
        f"Question: {question}"
    )
    try:
        return ask_gemini(prompt)
    except Exception as e:
        return f"Error: {e}"
