"""SQLAlchemy model placeholders for persisted application data."""

from __future__ import annotations

from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.session import Base


class UserLog(Base):
    """Persisted snapshot of user cognitive state."""

    __tablename__ = "user_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    sleep_hours: Mapped[float] = mapped_column(Float, nullable=False)
    stress_level: Mapped[int] = mapped_column(Integer, nullable=False)
    time_of_day: Mapped[str] = mapped_column(String(32), nullable=False)


class TaskRecord(Base):
    """Persisted study task entry."""

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    estimated_time: Mapped[int] = mapped_column(Integer, nullable=False)
    subject: Mapped[str] = mapped_column(String(128), nullable=False)

