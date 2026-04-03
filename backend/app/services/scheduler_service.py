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

        # We want harder tasks clustered around the preferred time, not to center the whole block.
        # Group tasks by difficulty and create an ordered list where hard tasks are contiguous in the middle
        hard = [t for t in tasks_sorted if self._difficulty_score(t.get("difficulty", "medium")) == 3]
        medium = [t for t in tasks_sorted if self._difficulty_score(t.get("difficulty", "medium")) == 2]
        easy = [t for t in tasks_sorted if self._difficulty_score(t.get("difficulty", "medium")) == 1]

        combined = medium + easy
        mid = len(combined) // 2
        pre = combined[:mid]
        post = combined[mid:]

        ordered = pre + hard + post

        # Break policy (minutes) after a task based on difficulty
        break_after = {
            "easy": 5,
            "medium": 10,
            "hard": 20
        }

        # compute total minutes including breaks
        total_task_minutes = sum(int(t.get("estimated_time", 60)) for t in ordered)
        total_break_minutes = sum(break_after.get(t.get("difficulty", "medium"), 10) for t in ordered)
        total_minutes = total_task_minutes + total_break_minutes

        # Primary work windows (hours) per preference — prefer to place hard tasks inside these when possible
        primary_windows = {
            "morning": (8, 12),
            "afternoon": (12, 17),
            "evening": (17, 21),
            "night": (21, 2),
        }

        window = primary_windows.get(preferred_time_of_day, (17, 21))

        # compute hard block minutes
        hard_minutes = sum(int(t.get("estimated_time", 60)) for t in hard) + sum(break_after.get(t.get("difficulty", "medium"), 10) for t in hard)

        # if window crosses midnight (night), treat window_end as +24 when needed
        wstart, wend = window
        window_length = (wend - wstart) if wend > wstart else (24 - wstart + wend)

        # Decide hard block start: try to center hard block inside primary window if it fits
        if hard and hard_minutes <= window_length * 60:
            # center hard block within window
            hard_start = wstart + (window_length * 60 - hard_minutes) / 120.0  # in hours
        else:
            # fallback: center on center_hour as before
            hard_start = center_hour - (hard_minutes / 60.0) / 2.0

        # compute minutes before hard block (pre) and after (post)
        minutes_before = sum(int(t.get("estimated_time", 60)) + break_after.get(t.get("difficulty", "medium"), 10) for t in pre)
        minutes_after = sum(int(t.get("estimated_time", 60)) + break_after.get(t.get("difficulty", "medium"), 10) for t in post)

        # start hour is hard_start minus minutes_before
        start_hour = hard_start - (minutes_before / 60.0)

        # Clamp schedule to reasonable daytime bounds to avoid pushing into deep night
        DAY_START = 6   # earliest hour to schedule
        DAY_END = 22    # latest hour we'd prefer to end

        # If start would be before DAY_START, push forward
        if start_hour < DAY_START:
            start_hour = DAY_START

        total_hours = total_minutes / 60.0
        if start_hour + total_hours > DAY_END:
            # push start earlier so it ends at DAY_END (if possible)
            start_hour = max(DAY_START, DAY_END - total_hours)

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