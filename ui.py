from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from voice import get_voice_input
import cv2


class Dashboard(QWidget):

    def __init__(self, env, model):
        super().__init__()
        self.env = env
        self.model = model
        self.current_image = None

        self.setWindowTitle("CLP AI Diagnosis System")
        self.setGeometry(200, 200, 400, 550)

        # 🌙 DARK THEME
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2f;
                color: white;
                font-size: 16px;
            }
            QPushButton {
                background-color: #3a86ff;
                color: white;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #265df2;
            }
            QLabel {
                color: white;
            }
        """)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.title = QLabel("CLP Diagnosis System")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-size: 22px; font-weight: bold;")

        self.image_label = QLabel("No Image")
        self.image_label.setFixedSize(250, 250)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("border: 2px solid white;")

        self.result_label = QLabel("Choose an option")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Buttons
        self.upload_btn = QPushButton("Upload Image")
        self.upload_btn.clicked.connect(self.upload_image)

        self.camera_btn = QPushButton("Use Camera")
        self.camera_btn.clicked.connect(self.open_camera)

        self.predict_btn = QPushButton("Start Diagnosis")
        self.predict_btn.clicked.connect(self.run_model)

        self.voice_btn = QPushButton("Voice Input")
        self.voice_btn.clicked.connect(self.use_voice)

        layout.addWidget(self.title)
        layout.addWidget(self.image_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.result_label)

        layout.addWidget(self.upload_btn)
        layout.addWidget(self.camera_btn)
        layout.addWidget(self.predict_btn)
        layout.addWidget(self.voice_btn)

        self.setLayout(layout)

    # 📁 Upload Image
    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.current_image = file_path
            self.show_image(file_path)

    # 📷 Camera Capture
    def open_camera(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow("Press SPACE to capture", frame)

            key = cv2.waitKey(1)
            if key == 32:  # SPACE
                img_path = "captured.jpg"
                cv2.imwrite(img_path, frame)
                self.current_image = img_path
                break
            elif key == 27:  # ESC
                break

        cap.release()
        cv2.destroyAllWindows()

        if self.current_image:
            self.show_image(self.current_image)

    # 🖼 Show Image
    def show_image(self, path):
        pixmap = QPixmap(path)
        if not pixmap.isNull():
            self.image_label.setPixmap(
                pixmap.scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio)
            )
        else:
            self.result_label.setText("Image load failed")

    # 🤖 Improved Prediction
    def run_model(self):
        if not self.current_image:
            self.result_label.setText("Please upload or capture image")
            return

        # Dummy smarter logic (replace later with ML model)
        import random
        action = random.choice([0, 1, 2])

        severity = ["Mild", "Moderate", "Severe"]

        self.result_label.setText(
            f"Prediction: {severity[action]}\nConfidence: {random.randint(70, 95)}%"
        )

    # 🎤 Voice Input
    def use_voice(self):
        self.result_label.setText("Listening...")

        text = get_voice_input()

        if text in ["timeout", "unknown", "error"]:
            self.result_label.setText("Voice error")
            return

        # smarter logic (priority)
        if "severe" in text:
            action = 2
        elif "moderate" in text:
            action = 1
        elif "mild" in text:
            action = 0
        else:
            self.result_label.setText(f"You said: {text}")
            return

        severity = ["Mild", "Moderate", "Severe"]

        self.result_label.setText(
            f"Voice Input: {text}\nDetected: {severity[action]}"
        )