from typing import List, Dict


class SchedulerService:
    """
    Generates a schedule based on energy levels and task difficulty.
    Pure logic — no ML, no API.
    """

    def __init__(self) -> None:
        pass

    def generate_schedule(self, energy: float, tasks: List[Dict]) -> List[Dict]:
        if not tasks:
            return []
        """
        Args:
            energy (float): 0–1
            tasks (list): [{title, estimated_time, difficulty}]

        Returns:
            list of scheduled tasks
        """

        # Step 1: sort tasks by difficulty (hard → easy)
        tasks_sorted = sorted(
            tasks,
            key=lambda x: self._difficulty_score(x.get("difficulty", "medium")),
            reverse=True
        )

        schedule = []
        current_time = 18  # start at 6 PM (can change later)

        for task in tasks_sorted:
            duration = task.get("estimated_time", 60)

            efficiency = self._estimate_efficiency(energy, task["difficulty"])

            schedule.append({
                "time_slot": self._format_time(current_time, duration),
                "task": task["title"],
                "expected_efficiency": round(efficiency, 2)
            })

            current_time += duration / 60  # increment hours

        return schedule

    # -------------------------
    # Helpers
    # -------------------------

    def _difficulty_score(self, difficulty: str) -> int:
        mapping = {
            "easy": 1,
            "medium": 2,
            "hard": 3
        }
        return mapping.get(difficulty, 2)

    def _estimate_efficiency(self, energy: float, difficulty: str) -> float:
        """
        Higher mismatch → lower efficiency
        """
        difficulty_map = {
            "easy": 0.4,
            "medium": 0.7,
            "hard": 1.0
        }

        diff_score = difficulty_map.get(difficulty, 0.7)

        return max(0.1, 1 - abs(diff_score - energy))

    def _format_time(self, start_hour: float, duration_min: int) -> str:
        start_h = int(start_hour)
        start_m = int((start_hour % 1) * 60)

        end_hour = start_hour + duration_min / 60
        end_h = int(end_hour)
        end_m = int((end_hour % 1) * 60)

        return f"{start_h:02d}:{start_m:02d}-{end_h:02d}:{end_m:02d}"