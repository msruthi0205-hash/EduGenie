"""Personalized learning path (Gemini)."""
from gemini_client import ask_gemini


def get_learning_recommendations(topic: str) -> str:
    prompt = (
        f"Create a structured learning path for the topic: {topic}.\n"
        "Organize it from Beginner to Intermediate to Advanced. For each level give:\n"
        "- Key concepts to learn\n- Estimated time\n"
        "- Useful resources (videos, articles or books)\n"
        "Finish with 3 practice project or exercise ideas. Keep it clear and well organized."
    )
    try:
        return ask_gemini(prompt)
    except Exception as e:
        return f"Error: {e}"
