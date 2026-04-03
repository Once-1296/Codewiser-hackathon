from typing import List, Dict


class SchedulerService:
    """
    Generates a schedule based on energy levels and task difficulty.
    Pure logic — no ML, no API.
    """

    def __init__(self) -> None:
        pass

    def generate_schedule(self, energy: float, tasks: List[Dict], preferred_time_of_day: str = "evening") -> List[Dict]:
        if not tasks:
            return []

        """
        Args:
            energy (float): 0–1
            tasks (list): [{title, estimated_time, difficulty}]
            preferred_time_of_day (str): one of 'morning', 'afternoon', 'evening', 'night'

        Returns:
            list of scheduled tasks with time_slot and expected_efficiency
        """

        # Step 1: sort tasks by difficulty (hard → easy) so we can place harder tasks
        tasks_sorted = sorted(
            tasks,
            key=lambda x: self._difficulty_score(x.get("difficulty", "medium")),
            reverse=True
        )

        # Determine preferred center hour for scheduling
        preferred_center_map = {
            "morning": 9,    # 9:00
            "afternoon": 14, # 14:00
            "evening": 19,   # 19:00
            "night": 22      # 22:00
        }
        center_hour = preferred_center_map.get(preferred_time_of_day, 19)

        # Order tasks so that harder tasks are placed closer to the center
        n = len(tasks_sorted)
        positions = list(range(n))
        center_point = (n - 1) / 2.0
        # sort positions by distance to center (closer positions first)
        positions.sort(key=lambda i: (abs(i - center_point), i))
        ordered = [None] * n
        for i, pos in enumerate(positions):
            ordered[pos] = tasks_sorted[i]

        # Break policy (minutes) after a task based on difficulty
        break_after = {
            "easy": 5,
            "medium": 10,
            "hard": 20
        }

        # compute total minutes including breaks to center the schedule
        total_task_minutes = sum(int(t.get("estimated_time", 60)) for t in ordered)
        total_break_minutes = sum(break_after.get(t.get("difficulty", "medium"), 10) for t in ordered)
        total_minutes = total_task_minutes + total_break_minutes

        # Start time is centered around preferred time
        total_hours = total_minutes / 60.0
        start_hour = center_hour - (total_hours / 2.0)

        schedule = []
        current_time = start_hour

        for task in ordered:
            duration = int(task.get("estimated_time", 60))
            difficulty = task.get("difficulty", "medium")

            efficiency = self._estimate_efficiency(energy, difficulty)

            schedule.append({
                "time_slot": self._format_time(current_time, duration),
                "task": task.get("title") or task.get("name") or "Study Block",
                "expected_efficiency": round(efficiency, 2),
                "difficulty": difficulty
            })

            # advance time by task duration
            current_time += duration / 60.0

            # insert a break after moderate/hard tasks to allow rest; small break for easy
            gap = break_after.get(difficulty, 10)
            current_time += gap / 60.0

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
        # Convert hours (may be fractional) to total minutes and normalize to 0-1439
        start_total_min = int(round(start_hour * 60))
        end_total_min = start_total_min + int(duration_min)

        MINUTES_PER_DAY = 24 * 60

        s = start_total_min % MINUTES_PER_DAY
        e = end_total_min % MINUTES_PER_DAY

        start_h = s // 60
        start_m = s % 60

        end_h = e // 60
        end_m = e % 60

        return f"{start_h:02d}:{start_m:02d}-{end_h:02d}:{end_m:02d}"