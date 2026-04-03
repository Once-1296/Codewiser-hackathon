"""Dependency injection helpers for API route handlers."""

from __future__ import annotations

from functools import lru_cache

from backend.app.ml.inference.energy_predictor import EnergyPredictor
from backend.app.ml.inference.task_classifier import TaskClassifier
from backend.app.services.energy_service import EnergyService
from backend.app.services.pipeline_service import PipelineService
from backend.app.services.scheduler_service import SchedulerService
from backend.app.services.task_service import TaskService


@lru_cache(maxsize=1)
def get_energy_predictor() -> EnergyPredictor:
    """Return a shared energy predictor instance."""

    return EnergyPredictor()


@lru_cache(maxsize=1)
def get_task_classifier() -> TaskClassifier:
    """Return a shared task classifier instance."""

    return TaskClassifier()


@lru_cache(maxsize=1)
def get_energy_service() -> EnergyService:
    """Return a shared energy service instance."""

    return EnergyService(predictor=get_energy_predictor())


@lru_cache(maxsize=1)
def get_task_service() -> TaskService:
    """Return a shared task service instance."""

    return TaskService(classifier=get_task_classifier())


@lru_cache(maxsize=1)
def get_scheduler_service() -> SchedulerService:
    """Return a shared scheduler service instance."""

    return SchedulerService()


@lru_cache(maxsize=1)
def get_pipeline_service() -> PipelineService:
    """Return a shared pipeline service instance."""

    return PipelineService(
        energy_service=get_energy_service(),
        task_service=get_task_service(),
        scheduler_service=get_scheduler_service(),
    )

