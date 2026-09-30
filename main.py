"""EduGenie - FastAPI app. Run with: uvicorn main:app --reload"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from explanation_module import explain_concept
from learning_path import get_learning_recommendations
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text

app = FastAPI(title="EduGenie")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class TextIn(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.post("/qa")
def qa(body: TextIn):
    return {"result": answer_question(body.text)}


@app.post("/explain")
def explain(body: TextIn):
    return {"result": explain_concept(body.text)}


@app.post("/quiz")
def quiz(body: TextIn):
    return {"result": generate_quiz(body.text)}


@app.post("/summarize")
def summarize(body: TextIn):
    return {"result": summarize_text(body.text)}


@app.post("/learn/recommendations")
def learn(body: TextIn):
    return {"result": get_learning_recommendations(body.text)}
