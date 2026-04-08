import sys
from PyQt6.QtWidgets import QApplication

from environment import CLPEnvironment
from model import CLPModel
from ui import Dashboard

app = QApplication(sys.argv)

env = CLPEnvironment()
model = CLPModel()

window = Dashboard(env, model)
window.show()

sys.exit(app.exec())