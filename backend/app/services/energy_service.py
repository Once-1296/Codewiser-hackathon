"""Service layer for energy prediction orchestration."""

from __future__ import annotations

from backend.app.ml.inference.energy_predictor import EnergyPredictor
from backend.app.schemas.user import EnergyPredictionResponse, UserState


class EnergyService:
    """Coordinate user-state feature preparation and energy inference."""

    def __init__(self, predictor: EnergyPredictor) -> None:
        """Create a new energy service with an injected predictor."""

        self._predictor = predictor

    def predict_energy(self, user_state: UserState) -> EnergyPredictionResponse:
        """Return a placeholder energy prediction for the given user state."""

        energy_level = self._predictor.predict(user_state)
        label = "high" if energy_level >= 0.7 else "moderate"
        explanation = "Placeholder inference result from the energy predictor."
        return EnergyPredictionResponse(
            energy_level=energy_level,
            label=label,
            explanation=explanation,
        )

