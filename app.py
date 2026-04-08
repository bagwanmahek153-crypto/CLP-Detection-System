import gradio as gr
import numpy as np
from PIL import Image

def predict(image):
    img = np.array(image)
    avg_pixel = img.mean()

    if avg_pixel > 150:
        return "Mild CLP"
    elif avg_pixel > 100:
        return "Moderate CLP"
    else:
        return "Severe CLP"

gr.Interface(fn=predict, inputs="image", outputs="text").launch()