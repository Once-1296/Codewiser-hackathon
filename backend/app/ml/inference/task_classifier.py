from typing import Dict
from backend.app.ml.features.feature_engineering import build_task_features

class TaskClassifier:
    """
    Classifies task difficulty into: easy, medium, hard.

    Current implementation is rule-based.
    Can later be replaced with ML model without changing interface.
    """

    def __init__(self) -> None:
        pass

    def classify(self, task: Dict) -> str:
        """
        Args:
            task (dict): {
                "title": str,
                "estimated_time": int (minutes),
                "subject": str
            }

        Returns:
            str: "easy" | "medium" | "hard"
        """

        time_score = self._score_time(task.get("estimated_time", 30))
        subject_score = self._score_subject(task.get("subject", ""))

        total_score = 0.7 * time_score + 0.3 * subject_score

        return self._map_to_label(total_score)

    # -------------------------
    # Feature helpers (PURE)
    # -------------------------

    def _score_time(self, minutes: int) -> float:
        """Longer tasks are harder."""
        if minutes <= 30:
            return 0.3
        elif minutes <= 90:
            return 0.6
        else:
            return 1.0

    def _score_subject(self, subject: str) -> float:
        """Assign rough difficulty weights per subject."""
        subject = subject.lower()

        mapping = {
            "math": 0.9,
            "dsa": 1.0,
            "physics": 0.9,
            "coding": 0.8,
            "history": 0.5,
            "english": 0.4
        }

        return mapping.get(subject, 0.6)

    def _map_to_label(self, score: float) -> str:
        """Convert numeric score → category."""
        if score < 0.4:
            return "easy"
        elif score < 0.75:
            return "medium"
        return "hard"
    
    def classify(self, task: Dict) -> str:
        features = build_task_features(task)

        total_score = (
            0.7 * features["time_score"] +
            0.3 * features["subject_score"]
        )

        return self._map_to_label(total_score)