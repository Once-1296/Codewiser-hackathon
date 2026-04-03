"""Health check route for liveness probes and quick validation."""

from __future__ import annotations

from fastapi import APIRouter

from backend.app.schemas.common import APIResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=APIResponse[dict[str, str]])
def health_check() -> APIResponse[dict[str, str]]:
    """Return a minimal health payload."""

    return APIResponse(
        message="Service is healthy",
        data={"status": "ok"},
    )

