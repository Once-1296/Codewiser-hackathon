import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

MODEL_PATH = "backend/app/ml/models/task_model.pkl"

from backend.training.dataset_loader import generate_task_dataset
def load_data():
    return generate_task_dataset(1000)


from backend.app.ml.features.feature_engineering import extract_keyword_score


def preprocess(df):
    subject_map = {
        "dsa": 1.0,
        "math": 0.9,
        "physics": 0.8,
        "english": 0.4,
        "history": 0.3
    }

    df["subject_score"] = df["subject"].map(subject_map)

    # simulate title for synthetic data
    df["title"] = df["subject"] + " practice"

    df["keyword_score"] = df["title"].apply(extract_keyword_score)

    X = df[["estimated_time", "subject_score", "keyword_score"]]
    y = df["difficulty"]

    return X, y


def train():
    df = load_data()
    X, y = preprocess(df)

    model = DecisionTreeClassifier()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    print("Task model saved!")


if __name__ == "__main__":
    train()