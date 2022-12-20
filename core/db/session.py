import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config.config import settings

"""
if you install postgres or any database

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
"""

"""
if you don't want to install postgres or any database, use sqlite,
a file system based database, uncomment below lines if you would like
to use sqlite and comment above 2 lines of SQLALCHEMY_DATABASE_URL AND engine
"""

SQLALCHEMY_DATABASE_URL = f"sqlite:///./{os.getenv('DATABASE_NAME', 'prod')}.sqlite3"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
