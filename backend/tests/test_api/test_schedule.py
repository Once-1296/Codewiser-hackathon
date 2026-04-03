from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_generate_schedule_api():
    payload = {
        "user_state": {
            "sleep_hours": 7,
            "stress_level": 2,
            "time_of_day": "morning"
        },
        "tasks": [
            {"title": "Read", "estimated_time": 30, "subject": "english"},
            {"title": "DSA", "estimated_time": 120, "subject": "dsa"}
        ]
    }

    response = client.post("/schedule/generate", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "schedule" in data
    assert isinstance(data["schedule"], list)