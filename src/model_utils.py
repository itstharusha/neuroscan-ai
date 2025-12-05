
from pathlib import Path
import joblib
import numpy as np

BASE = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE / "models" / "neuro_model_v1.joblib"
SCALER_PATH = BASE / "models" / "scaler.joblib"
ENCODER_PATH = BASE / "models" / "label_encoders.joblib"
SCHEMA_PATH = BASE / "input_schema.txt"

def load_objects():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    encoders = joblib.load(ENCODER_PATH)
    with open(SCHEMA_PATH, "r") as f:
        schema = [line.strip() for line in f.readlines()]
    return model, scaler, encoders, schema

def preprocess_input(raw: dict, scaler, encoders, schema):
    X = []
    for feature in schema:
        val = raw.get(feature, 0)
        if feature in encoders:
            val = encoders[feature].transform([val])[0]
        X.append(val)
    X = np.array(X).reshape(1, -1)
    X = scaler.transform(X)
    return X

def predict(model, X):
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(X)
        return float(proba[0][1])
    return int(model.predict(X)[0])
