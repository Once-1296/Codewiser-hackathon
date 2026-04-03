import pytest
from backend.app.ml.inference.task_classifier import TaskClassifier


@pytest.fixture
def classifier():
    return TaskClassifier()


def test_easy_task(classifier):
    task = {
        "title": "Read notes",
        "estimated_time": 20,
        "subject": "english"
    }

    result = classifier.classify(task)
    assert result == "easy"


def test_medium_task(classifier):
    task = {
        "title": "Practice problems",
        "estimated_time": 60,
        "subject": "history"
    }

    result = classifier.classify(task)
    assert result == "medium"


def test_hard_task(classifier):
    task = {
        "title": "DP problems",
        "estimated_time": 120,
        "subject": "dsa"
    }

    result = classifier.classify(task)
    assert result == "hard"


def test_unknown_subject(classifier):
    task = {
        "title": "Something random",
        "estimated_time": 45,
        "subject": "unknown"
    }

    result = classifier.classify(task)
    assert result in ["easy", "medium", "hard"]