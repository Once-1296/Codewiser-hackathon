"""Placeholder feature engineering functions for study planner ML."""

from __future__ import annotations

from backend.app.schemas.task import Task
from backend.app.schemas.user import UserState


def build_energy_features(user_state: UserState) -> dict[str, float | str]:
    """Build stub features for the energy predictor."""

    return {
        "sleep_hours": user_state.sleep_hours,
        "stress_level": float(user_state.stress_level),
        "time_of_day": user_state.time_of_day,
    }


def build_task_features(task: Task) -> dict[str, float | str]:
    """Build stub features for the task classifier."""

    return {
        "title_length": float(len(task.title)),
        "estimated_time": float(task.estimated_time),
        "subject": task.subject,
    }


def build_features(payload: dict[str, object]) -> dict[str, object]:
    """Generic placeholder feature builder for future expansion."""

    return payload

