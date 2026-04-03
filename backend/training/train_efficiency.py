import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
try:
    import lightgbm as lgb
except ImportError:
    print("lightgbm is not installed. Install it with: pip install lightgbm")
    raise

DATA = "backend/training/efficiency_dataset.csv"
OUT = "backend/app/ml/models/efficiency_model.pkl"

os.makedirs(os.path.dirname(OUT), exist_ok=True)

print("Loading dataset...")
df = pd.read_csv(DATA)

# features and label
X = df.drop(columns=["label"])
y = df["label"]

# simple train/test split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.15, random_state=42)

print("Training LightGBM regressor (sklearn API)...")
model = lgb.LGBMRegressor(objective="regression", n_estimators=200, random_state=42)

# fit with early stopping using sklearn API
model.fit(
    X_train,
    y_train,
    eval_set=[(X_val, y_val)],
    eval_metric="rmse",
    callbacks=[lgb.early_stopping(20)],
)

print("Saving model...")
joblib.dump(model, OUT)
print(f"Model saved to {OUT}")
