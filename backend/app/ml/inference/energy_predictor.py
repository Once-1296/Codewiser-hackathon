from typing import Dict
from backend.app.ml.features.feature_engineering import build_energy_features

class EnergyPredictor:
    """
    Predicts cognitive energy score (0 to 1) based on user state.

    This is currently a rule-based baseline.
    Can be replaced later with a trained ML model without changing interface.
    """

    def __init__(self) -> None:
        # Placeholder for future model loading
        pass

    def predict(self, user_state: Dict) -> float:
        """
        Main prediction method.

        Args:
            user_state (dict): {
                "sleep_hours": float,
                "stress_level": int (1–5),
                "time_of_day": str ("morning", "afternoon", "evening", "night")
            }

        Returns:
            float: energy score between 0 and 1
        """

        sleep = self._normalize_sleep(user_state.get("sleep_hours", 0))
        stress = self._normalize_stress(user_state.get("stress_level", 3))
        time_score = self._encode_time_of_day(user_state.get("time_of_day", "afternoon"))

        energy = (
            0.5 * sleep +
            0.3 * stress +
            0.2 * time_score
        )

        return self._clamp(energy)

    # -------------------------
    # Feature helpers (PURE)
    # -------------------------

    def _normalize_sleep(self, sleep_hours: float) -> float:
        """Normalize sleep to 0–1 range (ideal = 8h)."""
        return min(max(sleep_hours / 8.0, 0), 1)

    def _normalize_stress(self, stress_level: int) -> float:
        """Invert stress (lower stress = higher energy)."""
        stress_level = min(max(stress_level, 1), 5)
        return 1 - ((stress_level - 1) / 4)

    def _encode_time_of_day(self, time_of_day: str) -> float:
        """Map time of day to energy score."""
        mapping = {
            "morning": 1.0,
            "afternoon": 0.8,
            "evening": 0.6,
            "night": 0.4
        }
        return mapping.get(time_of_day.lower(), 0.7)

    def _clamp(self, value: float) -> float:
        """Ensure output stays between 0 and 1."""
        return max(0.0, min(1.0, value))



    def predict(self, user_state: Dict) -> float:
        features = build_energy_features(user_state)

        energy = (
            0.5 * features["sleep_normalized"] +
            0.3 * features["stress_normalized"] +
            0.2 * features["time_score"]
        )

        return self._clamp(energy)