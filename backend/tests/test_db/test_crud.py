from backend.app.db.session import SessionLocal
from backend.app.db import crud


def test_create_user():
    db = SessionLocal()

    user = {
        "sleep_hours": 6,
        "stress_level": 3,
        "time_of_day": "evening"
    }

    result = crud.create_user_state(db, user)

    assert result.id is not None


def test_create_tasks():
    db = SessionLocal()

    tasks = [
        {"title": "Read", "estimated_time": 30, "subject": "english"},
    ]

    result = crud.create_tasks(db, tasks)

    assert len(result) == 1