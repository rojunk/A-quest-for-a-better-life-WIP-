from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer
import math
import sys

app = QApplication(sys.argv)

# Window setup
window = QWidget()
window.resize(1600, 900)
window.setWindowTitle("Quest for the Dream Job")

# Title text to animate
text = "Q u e s t    f o r    t h e    D r e a m    J o b"
labels = []

# Create QLabel for each character and add to the window
font = QFont("Fira Sans", 36)
start_x = (window.width() - len(text) * 20) // 2  # Calculate start position for centering
y = 200

for i, char in enumerate(text):
    label = QLabel(char, window)
    label.setFont(font)
    label.move(start_x + i * 20, y)  # Position labels horizontally with some spacing
    labels.append(label)
    label.show()

# Wave variables
wave_amplitude = 10
wave_frequency = 0.3
counter = 0

# Wave function to animate the labels
def title_wave():
    global counter
    for i, label in enumerate(labels):
        offset = math.sin(counter * wave_frequency + i) * wave_amplitude
        label.move(label.x(), y + int(offset))
  # Update vertical position for each label

    counter += 1

# Timer for animation
timer = QTimer()
timer.timeout.connect(title_wave)
timer.start(100)

window.show()
sys.exit(app.exec())

