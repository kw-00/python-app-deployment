from flask import Flask, render_template, request, redirect, url_for
from app.tasks import save_user_task
from app.models import init_db

app = Flask(__name__)

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sync", methods=["GET", "POST"])
def sync_form():
    if request.method == "POST":
        from app.db import engine
        from sqlalchemy import text

        name = request.form["name"]
        surname = request.form["surname"]

        with engine.begin() as conn:
            conn.execute(
                text("INSERT INTO users (name, surname) VALUES (:name, :surname)"),
                {"name": name, "surname": surname},
            )

        return redirect(url_for("sync_form"))

    return render_template("sync.html")

@app.route("/async", methods=["GET", "POST"])
def async_form():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]

        save_user_task.delay(name, surname)

        return render_template("async.html", queued=True)

    return render_template("async.html", queued=False)


@app.route("/users")
def users():
    from app.db import engine
    from sqlalchemy import text

    with engine.begin() as conn:
        result = conn.execute(text("SELECT id, name, surname FROM users ORDER BY id DESC"))
        users = result.mappings().all()

    return render_template("users.html", users=users)
