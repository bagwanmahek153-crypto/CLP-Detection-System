from fastapi import FastAPI
import numpy as np
import cv2
import base64

app = FastAPI()

# Reset endpoint
@app.post("/reset")
def reset():
    return {"message": "Environment reset successful"}

# Predict endpoint
@app.post("/predict")
def predict(data: dict):
    try:
        # Expecting base64 image
        image_data = data.get("image")

        # Decode base64 image
        image_bytes = base64.b64decode(image_data)
        np_arr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Prediction logic (your logic)
        avg_pixel = image.mean()

        if avg_pixel > 150:
            result = "Mild CLP"
        elif avg_pixel > 100:
            result = "Moderate CLP"
        else:
            result = "Severe CLP"

        return {"result": result}

    except Exception as e:
        return {"error": str(e)}