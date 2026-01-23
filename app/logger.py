import csv
import os
from datetime import datetime

LOG_FILE = os.path.join("logs", "predictions.csv")

def log_prediction(inputs: dict, prediction: int):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)

        # Write header only once
        if not file_exists:
            writer.writerow([
                "timestamp",
                "air_temperature",
                "process_temperature",
                "rotational_speed",
                "torque",
                "tool_wear",
                "prediction"
            ])

        writer.writerow([
            datetime.utcnow().isoformat(),
            inputs["air_temperature"],
            inputs["process_temperature"],
            inputs["rotational_speed"],
            inputs["torque"],
            inputs["tool_wear"],
            prediction
        ])
