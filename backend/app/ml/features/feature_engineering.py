from typing import Dict


# -------------------------
# ENERGY FEATURES
# -------------------------

def build_energy_features(user_state: Dict) -> Dict:
    """
    Convert raw user input → model-ready features.
    """

    return {
        "sleep_normalized": normalize_sleep(user_state.get("sleep_hours", 0)),
        "stress_normalized": normalize_stress(user_state.get("stress_level", 3)),
        "time_score": encode_time_of_day(user_state.get("time_of_day", "afternoon"))
    }


def normalize_sleep(sleep_hours: float) -> float:
    return min(max(sleep_hours / 8.0, 0), 1)


def normalize_stress(stress_level: int) -> float:
    stress_level = min(max(stress_level, 1), 5)
    return 1 - ((stress_level - 1) / 4)


def encode_time_of_day(time_of_day: str) -> float:
    mapping = {
        "morning": 1.0,
        "afternoon": 0.8,
        "evening": 0.6,
        "night": 0.4
    }
    return mapping.get(time_of_day.lower(), 0.7)


# -------------------------
# TASK FEATURES
# -------------------------

def build_task_features(task: Dict) -> Dict:
    return {
        "time_score": score_time(task.get("estimated_time", 30)),
        "subject_score": score_subject(task.get("subject", ""))
    }


def score_time(minutes: int) -> float:
    if minutes <= 30:
        return 0.3
    elif minutes <= 90:
        return 0.6
    return 1.0


def score_subject(subject: str) -> float:
    mapping = {
        "math": 0.9,
        "dsa": 1.0,
        "physics": 0.9,
        "coding": 0.8,
        "history": 0.5,
        "english": 0.4
    }
    return mapping.get(subject.lower(), 0.6)