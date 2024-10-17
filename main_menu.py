import os
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QFont
import sys

app = QApplication(sys.argv)

# Set working directory to the script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Window setup
window = QWidget()
window.resize(1600, 900)
window.setWindowTitle("Quest for the Dream Job")

# Set a background image for the window
window.setStyleSheet("background-image: url('menu_background.png'); background-repeat: no-repeat; background-position: center; background-size: cover;")

start_button = QPushButton("Start Game", window)

# Step 4: Set custom font for the button
custom_font = QFont("American Captain", 24)  # Set custom font with size 24
start_button.setFont(custom_font)
start_button.setStyleSheet("""
    background-color: transparent;
    border: none;
    color: #FF5733;
""")

start_button.move(700        , 400)

window.show()
sys.exit(app.exec())
