from typing import Dict


# -------------------------
# ENERGY FEATURES
# -------------------------

def build_energy_features(user_state: Dict) -> Dict:
    """
    Convert raw user input → model-ready features.
    """

    return {
        "sleep_normalised": normalize_sleep(user_state.get("sleep_hours", 0)),
        "stress_normalised": normalize_stress(user_state.get("stress_level", 3)),
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
        "subject_score": score_subject(task.get("subject", "")),
        "keyword_score": extract_keyword_score(task.get("title", ""))
    }


def build_efficiency_features(item: Dict, user_state: Dict, energy: float, position: int, cumulative_minutes: int, break_before: int) -> Dict:
    """
    Build features for efficiency model per scheduled task.
    item: scheduled entry or original task dict containing title, estimated_time, difficulty
    user_state: original user state dict (sleep_hours, stress_level, time_of_day)
    energy: predicted energy (0-1)
    position: index in schedule (0..n-1)
    cumulative_minutes: minutes scheduled before this task
    break_before: minutes of gap before this task
    """

    task = item
    tf = build_task_features(task)
    energy_feats = build_energy_features(user_state)

    start_hour = 0
    # try to parse start hour from time_slot if available: 'HH:MM-HH:MM'
    ts = item.get("time_slot") or ""
    try:
        if ts and "-" in ts:
            start = ts.split("-")[0]
            start_hour = int(start.split(":")[0]) + int(start.split(":")[1]) / 60.0
    except Exception:
        start_hour = 0

    features = {
        # task features
        "time_score": tf["time_score"],
        "subject_score": tf["subject_score"],
        "keyword_score": tf["keyword_score"],
        "estimated_time": int(task.get("estimated_time", 30)),
        # user / energy
        "sleep_hours": float(user_state.get("sleep_hours", 7)),
        "stress_level": int(user_state.get("stress_level", 3)),
        "energy_pred": float(energy),
        "time_of_day_score": float(energy_feats.get("time_score", 0)),
        # schedule context
        "start_hour": float(start_hour),
        "position": int(position),
        "cumulative_minutes": int(cumulative_minutes),
        "break_before": int(break_before),
        # difficulty encoded ordinal
        "difficulty": 2 if task.get("difficulty") == "medium" else (3 if task.get("difficulty") == "hard" else 1)
    }

    return features


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

def extract_keyword_score(title: str) -> float:
    title = title.lower()

    hard_keywords = ["dp", "dynamic", "graph", "optimize"]
    medium_keywords = ["practice", "exercise", "problem"]
    easy_keywords = ["read", "revise", "notes"]

    score = 0.5  # default

    for word in hard_keywords:
        if word in title:
            return 1.0

    for word in medium_keywords:
        if word in title:
            return 0.7

    for word in easy_keywords:
        if word in title:
            return 0.3

    return score