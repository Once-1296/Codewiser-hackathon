"""Service layer for task classification orchestration."""

from __future__ import annotations

from backend.app.ml.inference.task_classifier import TaskClassifier
from backend.app.schemas.task import Task, TaskClassificationResponse


class TaskService:
    """Coordinate task normalization and task classification."""

    def __init__(self, classifier: TaskClassifier) -> None:
        """Create a new task service with an injected classifier."""

        self._classifier = classifier

    def classify_task(self, task: Task) -> TaskClassificationResponse:
        """Return a placeholder task classification result."""

        task_type = self._classifier.classify(task)
        return TaskClassificationResponse(
            task_type=task_type,
            confidence=0.85,
            rationale="Placeholder classification result from the task classifier.",
        )

