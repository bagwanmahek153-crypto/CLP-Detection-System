import sys
import cv2
import numpy as np
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt


class CLPInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CLP Detection System")
        self.setGeometry(100, 100, 400, 500)

        # UI Elements
        self.image_label = QLabel("Upload Image")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.result_label = QLabel("Result: ")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.upload_btn = QPushButton("Upload Image")
        self.upload_btn.clicked.connect(self.load_image)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.upload_btn)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg)")

        if file_path:
            # Show image
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))

            # Process image
            img = cv2.imread(file_path)
            result = self.predict(img)

            # Show result
            self.result_label.setText(f"Result: {result}")

    def predict(self, image):
        # Simple rule-based logic
        avg_pixel = image.mean()

        if avg_pixel > 150:
            return "Mild CLP"
        elif avg_pixel > 100:
            return "Moderate CLP"
        else:
            return "Severe CLP"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CLPInterface()
    window.show()
    sys.exit(app.exec())