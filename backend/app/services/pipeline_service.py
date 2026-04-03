"""Service layer that orchestrates energy, task, and scheduling services."""

from __future__ import annotations

from backend.app.schemas.schedule import ScheduleGenerationRequest, SchedulePlan
from backend.app.services.energy_service import EnergyService
from backend.app.services.scheduler_service import SchedulerService
from backend.app.services.task_service import TaskService


class PipelineService:
    """Coordinate the end-to-end planning flow."""

    def __init__(
        self,
        energy_service: EnergyService,
        task_service: TaskService,
        scheduler_service: SchedulerService,
    ) -> None:
        """Create a pipeline service from its constituent collaborators."""

        self._energy_service = energy_service
        self._task_service = task_service
        self._scheduler_service = scheduler_service

    def generate_schedule(self, request: ScheduleGenerationRequest) -> SchedulePlan:
        """Run the placeholder pipeline and return a schedule plan."""

        _ = self._energy_service.predict_energy(request.user_state)
        task_types = [self._task_service.classify_task(task).task_type for task in request.tasks]
        return self._scheduler_service.generate(request=request, task_types=task_types)

