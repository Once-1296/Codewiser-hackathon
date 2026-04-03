try:
    import joblib
except ImportError:
    joblib = None
import os
from typing import List, Dict
from backend.app.ml.features.feature_engineering import build_efficiency_features

MODEL_PATH = "backend/app/ml/models/efficiency_model.pkl"


class EfficiencyPredictor:

    def __init__(self, model_path: str = MODEL_PATH):
        self.model = None
        if joblib and os.path.exists(model_path):
            try:
                self.model = joblib.load(model_path)
            except Exception:
                self.model = None

    def predict_schedule(self, schedule: List[Dict], user_state: Dict, energy: float) -> List[Dict]:
        """
        Given a schedule list (each item with at least title/estimated_time/difficulty/time_slot),
        predict expected_efficiency for each and return schedule with updated 'expected_efficiency'.
        If model is not available, return schedule unchanged.
        """
        if not self.model:
            return schedule

        feats = []
        # compute cumulative minutes and break before
        cumulative = 0
        # precompute gaps from time_slots if present
        last_end = None
        for idx, item in enumerate(schedule):
            # estimate break_before from time_slot strings if possible
            break_before = 0
            ts = item.get("time_slot")
            if ts and "-" in ts and last_end:
                # naive parse
                try:
                    start = ts.split("-")[0]
                    h, m = start.split(":")
                    smin = int(h) * 60 + int(m)
                    gap = smin - last_end
                    if gap < 0:
                        gap += 24 * 60
                    break_before = gap
                except Exception:
                    break_before = 0

            feats.append(build_efficiency_features(item, user_state, energy, idx, cumulative, break_before))
            dur = int(item.get("estimated_time", 30))
            cumulative += dur + break_before

            # set last_end
            if ts and "-" in ts:
                try:
                    end = ts.split("-")[1]
                    eh, em = end.split(":")
                    last_end = int(eh) * 60 + int(em)
                except Exception:
                    last_end = None

        # Convert features dicts to a 2D array in fixed order
        feature_cols = [
            "time_score", "subject_score", "keyword_score", "estimated_time",
            "sleep_hours", "stress_level", "energy_pred", "time_of_day_score",
            "start_hour", "position", "cumulative_minutes", "break_before", "difficulty"
        ]

        X = []
        for f in feats:
            X.append([f.get(c, 0) for c in feature_cols])

        try:
            preds = self.model.predict(X)
        except Exception:
            # model failed, return schedule unchanged
            return schedule

        # attach predictions (clamp to [0.0, 1.0])
        out = []
        for item, p in zip(schedule, preds):
            val = float(p)
            if val < 0:
                val = 0.0
            if val > 1:
                val = 1.0
            new_item = dict(item)
            new_item["expected_efficiency"] = round(val, 2)
            out.append(new_item)

        return out
