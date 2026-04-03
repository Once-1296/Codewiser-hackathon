"""Placeholder task classifier used by the service layer."""

from __future__ import annotations

from backend.app.ml.features.feature_engineering import build_task_features
from backend.app.schemas.task import Task


class TaskClassifier:
    """Return a deterministic task label for a study task."""

    def classify(self, task: Task) -> str:
        """Classify a task using stubbed feature extraction."""

        _ = build_task_features(task)
        return "focus_block"

