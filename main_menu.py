import os
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QSlider
from PyQt6.QtGui import QPalette, QBrush, QPixmap, QFont
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl, Qt
import sys
import math



app = QApplication(sys.argv)

# Set working directory to the script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Window setup
window = QWidget()
window.resize(1600, 900)
window.setWindowTitle("Quest for the Dream Job")

# Set a background image using QPalette
palette = QPalette()
background = QPixmap("menu_background.png")
scaled_background = background.scaled(window.size())  # Scale image to the window size
palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_background))
window.setPalette(palette)

#WINDOW DIMENSIONS
window_width = window.width()


#START BUTTON
start_button = QPushButton("Start Game", window)
custom_font = QFont("American Captain", 24)  # Set custom font with size 24
start_button.setFont(custom_font)
start_button.setStyleSheet("""
    QPushButton {
        background-color: transparent;
        color: #FF5733;
        padding: 10px;
        margin: 0px;
    }
    QPushButton:hover {
        color: #33FF57;  /* Change to a different color when hovered */
    }
""")
start_button_width = start_button.sizeHint().width()
start_xposition = (window_width - start_button_width) // 2
start_button.move(start_xposition, 530)

#LOAD BUTTON
load_button = QPushButton("Load Game", window)
custom_font = QFont("American Captain", 24)  # Set custom font with size 24
load_button.setFont(custom_font)
load_button.setStyleSheet("""
    QPushButton {
        background-color: transparent;
        color: #FF5733;
        padding: 10px;
        margin: 0px;
    }
    QPushButton:hover {
        color: #33FF57;  /* Change to a different color when hovered */
    }
""")
load_button_width = load_button.sizeHint().width()
load_xposition = (window_width - load_button_width) // 2
load_button.move(load_xposition, 595)

#ABOUT
about_button = QPushButton("About", window)
custom_font = QFont("American Captain", 24)  # Set custom font with size 24
about_button.setFont(custom_font)
about_button.setStyleSheet("""
    QPushButton {
        background-color: transparent;
        color: #FF5733;
        padding: 10px;
        margin: 0px;
    }
    QPushButton:hover {
        color: #33FF57;  /* Change to a different color when hovered */
    }
""")
about_button_width = about_button.sizeHint().width()
about_xposition = (window_width - about_button_width) // 2
about_button.move(about_xposition, 660)

#EXTRAS
extras_button = QPushButton("Extras", window)
custom_font = QFont("American Captain", 24)  # Set custom font with size 24
extras_button.setFont(custom_font)
extras_button.setStyleSheet("""
    QPushButton {
        background-color: transparent;
        color: #FF5733;
        padding: 10px;
        margin: 0px;
    }
    QPushButton:hover {
        color: #33FF57;  /* Change to a different color when hovered */
    }
""")
extras_button_width = extras_button.sizeHint().width()
extras_xposition = (window_width - extras_button_width) // 2
extras_button.move(extras_xposition, 725)

#EXIT
def exit_app():
    sys.exit()

exit_button = QPushButton("EXIT", window)
custom_font = QFont("American Captain", 24)  # Set custom font with size 24
exit_button.setFont(custom_font)
exit_button.setStyleSheet("""
    QPushButton {
        background-color: transparent;
        color: #FF5733;
        padding: 10px;
        margin: 0px;
    }
    QPushButton:hover {
        color: #33FF57;  /* Change to a different color when hovered */
    }
""")
exit_button_width = exit_button.sizeHint().width()
exit_xposition = (window_width - exit_button_width) // 2
exit_button.move(exit_xposition, 790)
exit_button.clicked.connect(exit_app)


#MUSIC
player = QMediaPlayer()
audio_output = QAudioOutput()
player.setAudioOutput(audio_output)
player.setSource(QUrl.fromLocalFile('menu_music.mp3'))
player.setLoops(QMediaPlayer.Loops.Infinite)
player.play()

# Volume Slider setup
volume_slider = QSlider(Qt.Orientation.Horizontal, window)
volume_slider.setRange(0, 100)  # Volume range from 0 to 100
volume_slider.setValue(50)  # Set default volume to 50%
volume_slider.setGeometry(window.width() - 250, window.height() - 50, 200, 20)  # Position in the right-hand corner


# Function to apply volume using a logarithmic conversion
def apply_volume(value):
    # Convert the slider value (0-100) to a logarithmic volume (0.0 to 1.0)
    if value == 0:
        linear_volume = 0.0
    else:
        linear_volume = math.pow(value / 100.0, 2)  # Using a power of 2 to approximate a logarithmic curve

    audio_output.setVolume(linear_volume)

# Connect slider to volume change function
volume_slider.valueChanged.connect(apply_volume)

window.show()
sys.exit(app.exec())
