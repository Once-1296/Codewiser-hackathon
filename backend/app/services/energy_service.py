from typing import Dict
from backend.app.ml.inference.energy_predictor import EnergyPredictor


class EnergyService:
    """
    Handles energy prediction logic.
    Wraps ML layer — isolates it from rest of system.
    """

    def __init__(self) -> None:
        self.predictor = EnergyPredictor()

    def predict_energy(self, user_state: Dict) -> float:
        return self.predictor.predict(user_state)