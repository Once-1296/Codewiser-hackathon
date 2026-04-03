"""Placeholder energy predictor used by the service layer."""

from __future__ import annotations

from backend.app.ml.features.feature_engineering import build_energy_features
from backend.app.schemas.user import UserState


class EnergyPredictor:
    """Return a deterministic energy score for a user state."""

    def predict(self, user_state: UserState) -> float:
        """Predict cognitive energy using stubbed feature extraction."""

        _ = build_energy_features(user_state)
        return 0.72

