from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_create_tasks():
    payload = [
        {"title": "Read", "estimated_time": 30, "subject": "english"},
        {"title": "DSA", "estimated_time": 120, "subject": "dsa"}
    ]

    response = client.post("/tasks/", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert data[0]["title"] == "Read"