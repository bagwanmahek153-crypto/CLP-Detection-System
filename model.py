import cv2
import random

class CLPModel:

    def predict(self, state):
        image_path = state["image"]

        # Load image
        img = cv2.imread(image_path)

        if img is None:
            return random.randint(0, 2)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Simple logic (placeholder for ML)
        avg_pixel = gray.mean()

        # Dummy classification logic
        if avg_pixel > 150:
            return 0   # mild
        elif avg_pixel > 100:
            return 1   # moderate
        else:
            return 2   # severe