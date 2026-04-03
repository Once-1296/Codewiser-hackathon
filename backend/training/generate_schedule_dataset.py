"""
Generate a synthetic dataset for efficiency regressor.
Produces CSV with features compatible with build_efficiency_features.
"""
import csv
import random
import os
from backend.app.services.scheduler_service import SchedulerService
from backend.app.services.task_service import TaskService
from backend.app.services.energy_service import EnergyService
from backend.app.ml.features.feature_engineering import build_efficiency_features

OUT = "backend/training/efficiency_dataset.csv"
N_SAMPLES = 2000

random.seed(42)

# small pool of titles and subjects
TITLES = [
    "Solve dynamic programming problems",
    "Read chapter on gravity",
    "Practice linked lists",
    "Review notes",
    "Work on project",
    "Math exercises",
    "Read research paper",
    "Memorize dates",
]
SUBJECTS = ["dsa", "physics", "math", "english", "history", "coding"]

scheduler = SchedulerService()
classifier = TaskService()
energy_srv = EnergyService()

# header
cols = [
    "time_score", "subject_score", "keyword_score", "estimated_time",
    "sleep_hours", "stress_level", "energy_pred", "time_of_day_score",
    "start_hour", "position", "cumulative_minutes", "break_before", "difficulty",
    "label"
]

os.makedirs(os.path.dirname(OUT), exist_ok=True)

with open(OUT, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(cols)

    for _ in range(N_SAMPLES):
        # sample user state
        user_state = {
            "sleep_hours": round(random.uniform(4, 9), 2),
            "stress_level": random.randint(1, 5),
            "time_of_day": random.choice(["morning", "afternoon", "evening", "night"])
        }

        energy = energy_srv.predict_energy(user_state)

        # generate a random task list length
        nt = random.randint(1, 6)
        tasks = []
        for i in range(nt):
            t = {
                "title": random.choice(TITLES),
                "estimated_time": random.choice([15, 30, 45, 60, 90, 120]),
                "subject": random.choice(SUBJECTS)
            }
            tasks.append(t)

        # classify/enrich
        enriched = classifier.classify_tasks(tasks)

        # schedule (centered)
        schedule = scheduler.generate_schedule(energy=energy, tasks=enriched, preferred_time_of_day=user_state["time_of_day"])[:]

        # compute label using scheduler's heuristic + fatigue/noise
        cumulative = 0
        last_end = None
        for idx, item in enumerate(schedule):
            # compute break_before
            break_before = 0
            ts = item.get("time_slot")
            if ts and "-" in ts and last_end:
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

            feats = build_efficiency_features(item, user_state, energy, idx, cumulative, break_before)

            # base label: reuse scheduler heuristic if available
            # replicate _estimate_efficiency behaviour
            diff_map = {"easy": 0.4, "medium": 0.7, "hard": 1.0}
            diff_score = diff_map.get(item.get("difficulty", "medium"), 0.7)
            base = max(0.1, 1 - abs(diff_score - energy))

            # fatigue penalty: small linear penalty with cumulative minutes
            fatigue = max(0.6, 1 - (cumulative / 480.0) * 0.2)
            # short break bonus
            break_bonus = 1.0 + min(0.15, break_before / 60.0 * 0.05)

            label = base * fatigue * break_bonus

            # add noise
            label = label + random.normalvariate(0, 0.05)
            label = max(0.0, min(1.0, label))

            row = [feats[c] for c in cols[:-1]]
            row.append(label)
            writer.writerow(row)

            dur = int(item.get("estimated_time", 30))
            cumulative += dur + break_before

            if ts and "-" in ts:
                try:
                    end = ts.split("-")[1]
                    eh, em = end.split(":")
                    last_end = int(eh) * 60 + int(em)
                except Exception:
                    last_end = None

print(f"Wrote dataset to {OUT}")
