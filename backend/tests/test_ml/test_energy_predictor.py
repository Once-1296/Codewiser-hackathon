

import pytest
from backend.app.ml.inference.energy_predictor import EnergyPredictor


@pytest.fixture
def predictor():
    return EnergyPredictor()


def test_energy_with_good_conditions(predictor):
    user = {
        "sleep_hours": 8,
        "stress_level": 1,
        "time_of_day": "morning"
    }

    energy = predictor.predict(user)

    assert 0.8 <= energy <= 1.0


def test_energy_with_bad_conditions(predictor):
    user = {
        "sleep_hours": 3,
        "stress_level": 5,
        "time_of_day": "night"
    }

    energy = predictor.predict(user)

    assert 0.0 <= energy <= 0.4


def test_energy_bounds(predictor):
    user = {
        "sleep_hours": 100,
        "stress_level": -10,
        "time_of_day": "unknown"
    }

    energy = predictor.predict(user)

    assert 0.0 <= energy <= 1.0


def test_missing_fields(predictor):
    user = {}

    energy = predictor.predict(user)

    assert 0.0 <= energy <= 1.0


