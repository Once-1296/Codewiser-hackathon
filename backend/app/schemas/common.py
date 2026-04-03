"""Common schema types shared across API responses."""

from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class APIResponse(BaseModel, Generic[T]):
    """Generic wrapper for API responses."""

    message: str = Field(..., description="Human-readable response message.")
    data: T | None = Field(default=None, description="Response payload.")


class ErrorResponse(BaseModel):
    """Standard error payload for predictable API failures."""

    message: str = Field(..., description="Human-readable error message.")
    details: dict[str, Any] | None = Field(
        default=None,
        description="Optional machine-readable details.",
    )

