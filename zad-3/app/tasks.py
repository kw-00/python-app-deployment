from app.celery_app import celery
from app.db import engine
from sqlalchemy import text

@celery.task
def save_user_task(name, surname):
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO users (name, surname) VALUES (:name, :surname)"),
            {"name": name, "surname": surname},
        )
