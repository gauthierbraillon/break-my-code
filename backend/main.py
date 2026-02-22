from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI(title="Break My Code")

FRONTEND = Path(__file__).parent.parent / "frontend" / "index.html"


@app.get("/", response_class=HTMLResponse)
async def homepage():
    return FRONTEND.read_text()
