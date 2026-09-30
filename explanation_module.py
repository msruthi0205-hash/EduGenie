"""Concept explanation using the local LaMini-Flan-T5-783M model.

If transformers/torch are not installed (or the model can't load),
we fall back to Gemini so the app still works.
"""
from gemini_client import ask_gemini

MODEL_ID = "MBZUAI/LaMini-Flan-T5-783M"
_pipe = None
_local_failed = False


def _load_local():
    global _pipe, _local_failed
    if _pipe is not None or _local_failed:
        return _pipe
    try:
        from transformers import pipeline
        _pipe = pipeline("text2text-generation", model=MODEL_ID)  # downloads ~3 GB on first run
    except Exception as e:
        print(f"[EduGenie] Local model unavailable ({e}). Falling back to Gemini.")
        _local_failed = True
    return _pipe


def explain_concept(concept: str) -> str:
    pipe = _load_local()
    if pipe is not None:
        try:
            prompt = f"Explain the following concept in simple words for a beginner: {concept}"
            out = pipe(prompt, max_length=256, do_sample=True, temperature=0.4)
            return out[0]["generated_text"].strip()
        except Exception as e:
            return f"Error: {e}"
    try:
        return ask_gemini(f"Explain this concept in simple words for a beginner, with a small example: {concept}")
    except Exception as e:
        return f"Error: {e}"
