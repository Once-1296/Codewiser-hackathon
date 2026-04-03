"""Schemas describing study tasks and task classification results."""

from __future__ import annotations

from pydantic import BaseModel, Field


class Task(BaseModel):
    """Input payload for a study task."""

    title: str = Field(..., min_length=1)
    estimated_time: int = Field(..., gt=0, description="Estimated time in minutes.")
    subject: str = Field(..., min_length=1)


class TaskClassificationResponse(BaseModel):
    """Response payload describing the inferred task class."""

    task_type: str = Field(..., min_length=1)
    confidence: float = Field(..., ge=0.0, le=1.0)
    rationale: str = Field(..., min_length=1)

