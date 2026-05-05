from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@db:5432/app",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
