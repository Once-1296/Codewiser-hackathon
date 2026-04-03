"""Tests for the application health endpoint."""

from __future__ import annotations

from backend.app.api.routes.health import health_check
from backend.app.main import app


def test_health_route_is_registered() -> None:
    """Verify the health route is registered on the FastAPI app."""

    assert any(getattr(route, "path", None) == "/health" for route in app.routes)


def test_health_endpoint_contract() -> None:
    """Verify the health endpoint function returns the expected payload."""

    payload = health_check()
    assert payload.message == "Service is healthy"
    assert payload.data == {"status": "ok"}
