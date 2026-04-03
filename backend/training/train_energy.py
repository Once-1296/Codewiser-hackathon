import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
from backend.training.dataset_loader import generate_energy_dataset
MODEL_PATH = "backend/app/ml/models/energy_model.pkl"


def load_data():
    return generate_energy_dataset(1000)


def preprocess(df):
    # basic feature engineering
    df["sleep_normalised"] = df["sleep_hours"] / 8
    df["stress_normalised"] = 1 - (df["stress_level"] - 1) / 4

    df["time_score"] = df["time_of_day"].map({
        "morning": 1.0,
        "afternoon": 0.8,
        "evening": 0.6,
        "night": 0.4
    }).fillna(0.7)

    X = df[["sleep_normalised", "stress_normalised", "time_score"]]
    y = df["energy_score"]

    return X, y


def train():
    df = load_data()
    X, y = preprocess(df)

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    print("Model saved!")


if __name__ == "__main__":
    train()