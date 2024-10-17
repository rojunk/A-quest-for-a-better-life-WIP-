from PyQt6.QtWidgets import QApplication, QLabel, QWidget
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Quest for the Dream Job")

title_label = QLabel("Quest for the Dream Job", window)
title_label.move(100,80)

window.showFullScreen()

sys.exit(app.exec())
