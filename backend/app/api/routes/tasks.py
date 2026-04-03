"""Task-related API routes for classification and intake."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from backend.app.api.deps import get_task_service
from backend.app.schemas.common import APIResponse
from backend.app.schemas.task import Task, TaskClassificationResponse
from backend.app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=APIResponse[TaskClassificationResponse])
def create_task(
    task: Task,
    task_service: TaskService = Depends(get_task_service),
) -> APIResponse[TaskClassificationResponse]:
    """Classify a task using the task service."""

    classification = task_service.classify_task(task)
    return APIResponse(message="Task classified", data=classification)

