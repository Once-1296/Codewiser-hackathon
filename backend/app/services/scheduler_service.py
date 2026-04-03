"""Service layer for constructing study schedules."""

from __future__ import annotations

from backend.app.schemas.schedule import ScheduleGenerationRequest, ScheduleItem, SchedulePlan


class SchedulerService:
    """Generate a deterministic schedule from input tasks and user state."""

    def generate(self, request: ScheduleGenerationRequest, task_types: list[str]) -> SchedulePlan:
        """Build a placeholder schedule plan using simple ordering rules."""

        items = [
            ScheduleItem(
                time_slot=f"slot-{index + 1}",
                task=task,
                expected_efficiency=0.8,
            )
            for index, task in enumerate(request.tasks)
        ]
        strategy = "energy-aware-placeholder"
        if task_types:
            strategy = f"{strategy}:{task_types[0]}"
        return SchedulePlan(items=items, total_tasks=len(items), strategy=strategy)

