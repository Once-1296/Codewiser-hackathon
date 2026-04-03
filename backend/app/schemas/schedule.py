"""Schemas describing schedule requests and generated plans."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

from backend.app.schemas.task import Task
from backend.app.schemas.user import UserState


class ScheduleItem(BaseModel):
    """A scheduled task entry paired with an efficiency estimate."""

    time_slot: str = Field(..., min_length=1)
    task: Task
    expected_efficiency: float = Field(..., ge=0.0, le=1.0)


class ScheduleGenerationRequest(BaseModel):
    """Input payload used to generate an optimized study schedule."""

    user_state: UserState
    tasks: list[Task]
    horizon: Literal["today", "tomorrow", "week"] = "today"


class SchedulePlan(BaseModel):
    """Generated plan returned by the scheduling pipeline."""

    items: list[ScheduleItem]
    total_tasks: int = Field(..., ge=0)
    strategy: str = Field(..., min_length=1)

