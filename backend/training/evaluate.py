"""Stub evaluation utilities for model validation."""

from __future__ import annotations


def evaluate(model_name: str) -> dict[str, float | str]:
    """Return placeholder metrics for a trained model."""

    return {"model": model_name, "accuracy": 0.0}

