from fastapi import FastAPI
from app.model import predict_failure
from app.schemas import SensorInput

app = FastAPI(title="Predictive Maintenance API")

@app.get("/")
def health_check():
    return {"status": "API running"}

@app.post("/predict")
def predict(data: SensorInput):
    features = [
        data.air_temperature_k,
        data.process_temperature_k,
        data.rotational_speed_rpm,
        data.torque_nm,
        data.tool_wear_min
    ]

    prediction = predict_failure(features)

    return {
        "failure_prediction": int(prediction),
        "status": "FAILURE" if prediction == 1 else "NORMAL"
    }
