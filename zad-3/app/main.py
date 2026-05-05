from flask import Flask, request, jsonify, render_template
from app.models import init_db
from app.tasks import save_user_task
from app.db import engine
from sqlalchemy import text

app = Flask(__name__, template_folder="templates")

init_db()

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/form")
def form():
    return render_template("form.html")

@app.post("/users")
def create_user():
    name = request.form["name"]
    surname = request.form["surname"]

    task = save_user_task.delay(name, surname)
    return jsonify({"task_id": task.id, "status": "queued"})

@app.get("/users")
def users():
    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT name, surname FROM users ORDER BY id DESC")
        ).fetchall()

    return render_template("users.html", users=rows)

@app.get("/health")
def health():
    return {"status": "ok"}
