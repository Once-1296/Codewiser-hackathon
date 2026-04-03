"""Tests for the orchestration pipeline service."""

from __future__ import annotations

from backend.app.api.deps import get_pipeline_service
from backend.app.schemas.schedule import ScheduleGenerationRequest
from backend.app.schemas.task import Task
from backend.app.schemas.user import UserState


def test_pipeline_flow() -> None:
    """Verify the pipeline service returns a deterministic schedule."""

    pipeline_service = get_pipeline_service()
    request = ScheduleGenerationRequest(
        user_state=UserState(sleep_hours=7.5, stress_level=3, time_of_day="morning"),
        tasks=[
            Task(title="Read chapter 1", estimated_time=45, subject="biology"),
            Task(title="Solve practice set", estimated_time=60, subject="math"),
        ],
    )

    schedule = pipeline_service.generate_schedule(request)

    assert schedule.total_tasks == 2
    assert schedule.items[0].time_slot == "slot-1"
    assert schedule.strategy.startswith("energy-aware-placeholder")

