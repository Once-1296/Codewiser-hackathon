"""Dataset loader placeholders for future training data pipelines."""

from __future__ import annotations

from typing import Any


def load_dataset(name: str) -> list[dict[str, Any]]:
    """Return a deterministic placeholder dataset."""

    return [{"dataset": name, "rows": 0}]

