import pandas as pd
import random


def generate_energy_dataset(n=1000):
    data = []

    for _ in range(n):
        sleep = random.uniform(3, 9)
        stress = random.randint(1, 5)
        time_of_day = random.choice(["morning", "afternoon", "evening", "night"])

        sleep_norm = min(sleep / 8, 1.0)
        stress_norm = 1 - (stress - 1) / 4

        time_map = {
            "morning": 1.0,
            "afternoon": 0.8,
            "evening": 0.6,
            "night": 0.4
        }

        energy = (
            0.5 * sleep_norm +
            0.3 * stress_norm +
            0.2 * time_map[time_of_day]
        )

        # clamp to [0, 1]
        energy = max(0.0, min(1.0, energy))

        data.append({
            "sleep_hours": sleep,
            "stress_level": stress,
            "time_of_day": time_of_day,
            "energy_score": energy
        })

    return pd.DataFrame(data)


def generate_task_dataset(n=1000):
    subjects = ["dsa", "math", "physics", "english", "history"]

    data = []

    for _ in range(n):
        time = random.randint(10, 180)
        subject = random.choice(subjects)

        # heuristic label
        if time > 100 or subject in ["dsa", "math"]:
            difficulty = "hard"
        elif time > 40:
            difficulty = "medium"
        else:
            difficulty = "easy"

        data.append({
            "estimated_time": time,
            "subject": subject,
            "difficulty": difficulty
        })

    return pd.DataFrame(data)