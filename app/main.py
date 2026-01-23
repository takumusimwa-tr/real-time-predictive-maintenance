from fastapi import FastAPI
from app.model import predict_failure
from app.schemas import SensorInput
from app.logger import log_prediction

app = FastAPI(title="Predictive Maintenance API")

@app.get("/")
def health_check():
    return {"status": "API running"}

@app.post("/predict")
def predict(data: SensorInput):
    features = [
        data.air_temperature,
        data.process_temperature,
        data.rotational_speed,
        data.torque,
        data.tool_wear
    ]

    prediction = predict_failure(features)

    log_prediction(data.model_dump(), prediction)

    return {
        "failure_prediction": int(prediction),
        "status": "FAILURE" if prediction != 0 else "NORMAL"
    }
