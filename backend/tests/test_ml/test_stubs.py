"""Tests for stub ML components."""

from __future__ import annotations

from backend.app.ml.inference.energy_predictor import EnergyPredictor
from backend.app.ml.inference.task_classifier import TaskClassifier
from backend.app.schemas.task import Task
from backend.app.schemas.user import UserState


def test_energy_predictor_stub() -> None:
    """Verify the energy predictor returns the placeholder value."""

    predictor = EnergyPredictor()
    result = predictor.predict(UserState(sleep_hours=8, stress_level=2, time_of_day="evening"))
    assert result == 0.72


def test_task_classifier_stub() -> None:
    """Verify the task classifier returns the placeholder label."""

    classifier = TaskClassifier()
    result = classifier.classify(Task(title="Review notes", estimated_time=30, subject="history"))
    assert result == "focus_block"

