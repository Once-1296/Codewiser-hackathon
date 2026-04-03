"""FastAPI application entrypoint for the study planner backend."""

from __future__ import annotations

from fastapi import FastAPI

from backend.app.api.routes.health import router as health_router
from backend.app.api.routes.schedule import router as schedule_router
from backend.app.api.routes.tasks import router as tasks_router
from backend.app.api.routes.user import router as user_router
from backend.app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend skeleton for a cognitive-aware study planner.",
)

app.include_router(health_router)
app.include_router(user_router)
app.include_router(tasks_router)
app.include_router(schedule_router)


@app.get("/", tags=["root"])
def root() -> dict[str, str]:
    """Return a simple root response for quick smoke checks."""

    return {"message": "Cognitive-Aware Study Planner API"}

