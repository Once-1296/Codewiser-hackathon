"""Validation helpers used by services and future domain rules."""

from __future__ import annotations

from backend.app.schemas.schedule import ScheduleGenerationRequest
from backend.app.schemas.task import Task
from backend.app.schemas.user import UserState


def validate_user_state(user_state: UserState) -> None:
    """Validate a user state payload using schema-level constraints."""

    _ = user_state


def validate_task(task: Task) -> None:
    """Validate a task payload using schema-level constraints."""

    _ = task


def validate_schedule_request(request: ScheduleGenerationRequest) -> None:
    """Validate a schedule generation request using schema-level constraints."""

    _ = request

