"""Shared Gemini helper used by every cloud-powered module."""
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
_client = None


def _get_client():
    global _client
    if _client is None:
        key = os.getenv("GEMINI_API_KEY")
        if not key:
            raise RuntimeError("GEMINI_API_KEY is not set. Create a .env file (see .env.example).")
        _client = genai.Client(api_key=key)
    return _client


def ask_gemini(prompt: str) -> str:
    """Send a prompt to Gemini and return the text reply."""
    response = _get_client().models.generate_content(model=MODEL_NAME, contents=prompt)
    if not response or not response.text:
        raise ValueError("Gemini returned an empty or blocked response.")
    return response.text.strip()
