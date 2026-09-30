# EduGenie: Gemini Powered Learning Assistant

Features: Q&A, concept explanation, quiz generation (3 MCQs), summarization, learning paths.
Stack: FastAPI + Jinja2 + HTML/CSS, Google Gemini (cloud), LaMini-Flan-T5-783M (local, optional).

## Setup
1. Install Python 3.10+ and check: `python --version`
2. Create a virtual environment (recommended):
   - Mac/Linux: `python -m venv venv && source venv/bin/activate`
   - Windows: `python -m venv venv && venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
   (Want a quick, light install? Delete the last three lines of requirements.txt.
   Explanations will then use Gemini instead of the local model.)
4. Get a free API key at https://aistudio.google.com/apikey
5. Copy `.env.example` to `.env` and paste your key.

## Run
`uvicorn main:app --reload`
Open http://127.0.0.1:8000

## API endpoints
POST /qa, /explain, /quiz, /summarize, /learn/recommendations  with JSON body `{"text": "..."}`
Interactive docs: http://127.0.0.1:8000/docs

## Files
main.py (FastAPI app) | gemini_client.py (shared Gemini helper) | explanation_module.py |
qna.py | quiz_module.py | summary_module.py | learning_path.py |
templates/index.html | static/style.css | requirements.txt | .env.example

## Notes
- Model name is set in `.env` (GEMINI_MODEL). Google retires old models, so if you get a
  "model not found" error, update it to a current one from https://ai.google.dev/gemini-api/docs/models
- Never commit your real `.env` file.
