from sqlalchemy import text
from app.db import engine

def init_db():
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                surname TEXT NOT NULL
            );
        """))
