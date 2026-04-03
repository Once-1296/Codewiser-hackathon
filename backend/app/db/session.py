"""SQLAlchemy session configuration for the application database."""

from __future__ import annotations

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from backend.app.core.config import get_settings

settings = get_settings()

engine = create_engine(settings.database_url, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""


def get_db_session() -> Generator[Session, None, None]:
    """Yield a database session for request-scoped access."""

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
