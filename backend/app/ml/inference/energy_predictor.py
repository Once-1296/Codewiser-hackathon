try:
    import joblib
except ImportError:
    joblib = None
import os
from backend.app.ml.features.feature_engineering import build_energy_features


class EnergyPredictor:

    def __init__(self, model_path="backend/app/ml/models/energy_model.pkl"):
        self.model = None

        if joblib and os.path.exists(model_path):
            self.model = joblib.load(model_path)

    def predict(self, user_state: dict) -> float:
        features = build_energy_features(user_state)

        if self.model:
            X = [[
                features["sleep_normalized"],
                features["stress_normalized"],
                features["time_score"]
            ]]
            return float(self.model.predict(X)[0])

        # fallback
        return self._fallback(features)

    def _fallback(self, features):
        return max(0.0, min(1.0,
            0.5 * features["sleep_normalized"] +
            0.3 * features["stress_normalized"] +
            0.2 * features["time_score"]
        ))