from backend.app.services.scheduler_service import SchedulerService


def test_scheduler_basic():
    scheduler = SchedulerService()

    tasks = [
        {"title": "Easy Task", "estimated_time": 30, "difficulty": "easy"},
        {"title": "Hard Task", "estimated_time": 90, "difficulty": "hard"},
    ]

    result = scheduler.generate_schedule(energy=0.8, tasks=tasks)

    assert len(result) == 2
    assert result[0]["task"] == "Hard Task"  # hard first


def test_efficiency_bounds():
    scheduler = SchedulerService()

    tasks = [
        {"title": "Task", "estimated_time": 60, "difficulty": "medium"},
    ]

    result = scheduler.generate_schedule(energy=0.2, tasks=tasks)

    assert 0 <= result[0]["expected_efficiency"] <= 1