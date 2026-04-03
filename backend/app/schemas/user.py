"""Schemas describing user cognitive state and energy predictions."""

from __future__ import annotations

from pydantic import BaseModel, Field


class UserState(BaseModel):
    """Input payload representing a user's cognitive state snapshot."""

    sleep_hours: float = Field(..., ge=0.0, le=24.0)
    stress_level: int = Field(..., ge=1, le=10)
    time_of_day: str = Field(..., min_length=1)


class EnergyPredictionResponse(BaseModel):
    """Response payload describing a predicted energy estimate."""

    energy_level: float = Field(..., ge=0.0, le=1.0)
    label: str = Field(..., min_length=1)
    explanation: str = Field(..., min_length=1)

