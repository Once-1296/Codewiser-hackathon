try:
    import joblib
except ImportError:
    joblib = None
import os
from backend.app.ml.features.feature_engineering import build_task_features


class TaskClassifier:

    def __init__(self, model_path="backend/app/ml/models/task_model.pkl"):
        self.model = None

        if joblib and os.path.exists(model_path):
            self.model = joblib.load(model_path)

    def classify(self, task: dict) -> str:
        features = build_task_features(task)

        if self.model:
            X = [[
                task.get("estimated_time", 30),
                features["subject_score"],
                features["keyword_score"]
            ]]
            return str(self.model.predict(X)[0])

        return self._fallback(features)

    def _fallback(self, features):
        score = (
            0.5 * features["time_score"] +
            0.3 * features["subject_score"] +
            0.2 * features["keyword_score"]
        )
        if score < 0.4:
            return "easy"
        elif score < 0.75:
            return "medium"
        return "hard"