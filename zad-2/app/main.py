from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy import text
from app.db import engine
from app.models import init_db
from app.tasks import save_user_task

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/sync", response_class=HTMLResponse)
def sync_get(request: Request):
    return templates.TemplateResponse("sync.html", {"request": request})

@app.post("/sync")
def sync_post(name: str = Form(...), surname: str = Form(...)):
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO users (name, surname) VALUES (:name, :surname)"),
            {"name": name, "surname": surname},
        )
    return RedirectResponse("/sync", status_code=303)

@app.get("/async", response_class=HTMLResponse)
def async_get(request: Request):
    return templates.TemplateResponse("async.html", {"request": request, "queued": False})

@app.post("/async", response_class=HTMLResponse)
def async_post(request: Request, name: str = Form(...), surname: str = Form(...)):
    save_user_task.delay(name, surname)
    return templates.TemplateResponse("async.html", {"request": request, "queued": True})

@app.get("/users", response_class=HTMLResponse)
def users(request: Request):
    with engine.begin() as conn:
        result = conn.execute(text("SELECT id, name, surname FROM users ORDER BY id DESC"))
        users = result.mappings().all()

    return templates.TemplateResponse("users.html", {"request": request, "users": users})
