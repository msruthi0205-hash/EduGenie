"""Summarization (Gemini)."""
from gemini_client import ask_gemini


def summarize_text(text: str) -> str:
    prompt = (
        "Summarize the following educational passage into a concise, easy-to-understand "
        "version for quick revision. Keep the core information, remove redundancy. "
        "Use short bullet points.\n\n"
        f"{text}"
    )
    try:
        return ask_gemini(prompt)
    except Exception as e:
        return f"Error: {e}"
