from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Predictive Maintenance API")

class SensorInput(BaseModel):
    temperature: float
    vibration: float
    rpm: int
    torque: float

@app.get("/")
def health_check():
    return {"status": "running"}

@app.post("/predict")
def predict(data: SensorInput):
    # Placeholder prediction (0.15).
    risk = 0.15
    return {
        "failure_probability": risk,
        "status": "NORMAL"
    }
