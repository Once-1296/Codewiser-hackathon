from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_log_user():
    payload = {
        "sleep_hours": 7,
        "stress_level": 2,
        "time_of_day": "morning"
    }

    response = client.post("/user/logs", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert data["sleep_hours"] == 7