from backend.app.ml.features.feature_engineering import (
    normalize_sleep,
    normalize_stress,
    encode_time_of_day,
    score_time,
    score_subject,
)


def test_normalize_sleep_bounds():
    assert 0 <= normalize_sleep(0) <= 1
    assert normalize_sleep(8) == 1
    assert normalize_sleep(100) == 1


def test_normalize_stress():
    assert normalize_stress(1) == 1.0  # best
    assert normalize_stress(5) == 0.0  # worst


def test_time_encoding():
    assert encode_time_of_day("morning") == 1.0
    assert encode_time_of_day("night") == 0.4
    assert 0 <= encode_time_of_day("unknown") <= 1


def test_score_time():
    assert score_time(20) < score_time(60) < score_time(120)


def test_score_subject():
    assert score_subject("dsa") >= score_subject("english")
    assert 0 <= score_subject("unknown") <= 1