from backend.app.services.pipeline_service import PipelineService


def test_full_pipeline():
    pipeline = PipelineService()

    user = {
        "sleep_hours": 7,
        "stress_level": 2,
        "time_of_day": "morning"
    }

    tasks = [
        {"title": "Read notes", "estimated_time": 30, "subject": "english"},
        {"title": "Solve DSA", "estimated_time": 120, "subject": "dsa"},
    ]

    result = pipeline.generate_plan(user, tasks)

    assert isinstance(result, list)
    assert len(result) == 2

    for item in result:
        assert "time_slot" in item
        assert "task" in item
        assert "expected_efficiency" in item