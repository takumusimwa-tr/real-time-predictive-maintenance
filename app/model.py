import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "model.joblib")

# Load model once when app starts
model = joblib.load(MODEL_PATH)

def predict_failure(features):
    """
    features: list of 5 sensor values
    """
    prediction = model.predict([features])
    return int(prediction[0])
