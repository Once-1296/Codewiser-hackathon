import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import joblib

from backend.training.dataset_loader import (
    generate_energy_dataset,
    generate_task_dataset
)


# -------------------------
# ENERGY MODEL EVALUATION
# -------------------------

def evaluate_energy():
    df = generate_energy_dataset(1000)

    df["sleep_norm"] = df["sleep_hours"] / 8
    df["stress_norm"] = 1 - (df["stress_level"] - 1) / 4
    df["time_score"] = df["time_of_day"].map({
        "morning": 1.0,
        "afternoon": 0.8,
        "evening": 0.6,
        "night": 0.4
    })

    X = df[["sleep_norm", "stress_norm", "time_score"]]
    y = df["energy_score"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = joblib.load("backend/app/ml/models/energy_model.pkl")
    preds = model.predict(X_test)

    mse = mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    print("\n=== Energy Model ===")
    print(f"MSE: {mse:.4f}")
    print(f"R2: {r2:.4f}")

    # Plot
    plt.figure()
    plt.scatter(y_test, preds, alpha=0.5)
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.title("Energy Model Predictions")
    plt.savefig("energy_eval.png")
    plt.close()


# -------------------------
# TASK MODEL EVALUATION
# -------------------------
from backend.app.ml.features.feature_engineering import extract_keyword_score
def evaluate_task():
    df = generate_task_dataset(1000)

    subject_map = {
        "dsa": 1.0,
        "math": 0.9,
        "physics": 0.8,
        "english": 0.4,
        "history": 0.3
    }

    df["subject_score"] = df["subject"].map(subject_map)

    # simulate title (same as training)
    df["title"] = df["subject"] + " practice"

    df["keyword_score"] = df["title"].apply(extract_keyword_score)

    X = df[["estimated_time", "subject_score", "keyword_score"]]
    y = df["difficulty"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = joblib.load("backend/app/ml/models/task_model.pkl")
    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)

    print("\n=== Task Model ===")
    print(f"Accuracy: {acc:.4f}")
    print(classification_report(y_test, preds))

    # Plot distribution
    plt.figure()
    plt.hist(preds, alpha=0.7, label="Predicted")
    plt.hist(y_test, alpha=0.5, label="Actual")
    plt.legend()
    plt.title("Task Difficulty Distribution")
    plt.savefig("task_eval.png")
    plt.close()


if __name__ == "__main__":
    evaluate_energy()
    evaluate_task()