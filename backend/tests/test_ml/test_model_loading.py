from backend.app.ml.inference.energy_predictor import EnergyPredictor


def test_model_or_fallback():
    predictor = EnergyPredictor()

    user = {
        "sleep_hours": 7,
        "stress_level": 2,
        "time_of_day": "morning"
    }

    result = predictor.predict(user)

    assert 0 <= result <= 1