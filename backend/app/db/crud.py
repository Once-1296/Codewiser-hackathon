"""CRUD helpers for database access.

These functions are intentionally minimal and exist to define a future
persistence boundary without coupling the rest of the application to ORM
details.
"""

from __future__ import annotations

from typing import Any


def create_user_log(db: Any, payload: dict[str, Any]) -> dict[str, Any]:
    """Stub for creating a user log row."""

    return {"created": True, "payload": payload}


def create_task(db: Any, payload: dict[str, Any]) -> dict[str, Any]:
    """Stub for creating a task row."""

    return {"created": True, "payload": payload}

