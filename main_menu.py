import os
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QSlider
from PyQt6.QtGui import QPalette, QBrush, QPixmap, QFont, QIcon
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl, Qt, QSize
import sys
import math


app = QApplication(sys.argv)

# Set working directory to the script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Window setup
window = QWidget()
window.resize(1600, 900)
window.setWindowTitle("Quest for the Dream Job")

#BACKGROUND IMAGE QPALETTE
palette = QPalette()
background = QPixmap("menu_background.png")
scaled_background = background.scaled(window.size())
palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_background))
window.setPalette(palette)

#WINDOW DIMENSIONS
window_width = window.width()


#START BUTTON
start_button = QPushButton("Start Game", window)
custom_font = QFont("American Captain", 24)
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
custom_font = QFont("American Captain", 24)
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
custom_font = QFont("American Captain", 24)
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
custom_font = QFont("American Captain", 24)
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
custom_font = QFont("American Captain", 24)
exit_button.setFont(custom_font)
exit_button.setStyleSheet("""
    QPushButton {
        background-color: transparent;
        color: #FF5733;
        padding: 10px;
        margin: 0px;
    }
    QPushButton:hover {
        color: #33FF57;
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

#VOLUME SLIDER
volume_slider = QSlider(Qt.Orientation.Horizontal, window)
volume_slider.setRange(0, 100)  # Volume range from 0 to 100
volume_slider.setValue(40)  # Default volume
volume_slider.setGeometry(window.width() - 250, window.height() - 50, 200, 20)
volume_slider.setStyleSheet("""
    QSlider::groove:horizontal {
        background: black;
        height: 8px;
        border-radius: 4px;
    }

    QSlider::handle:horizontal {
        background: #FF5733;
        border: 1px solid #5c5c5c;
        width: 9px;
        height: 9px;
        margin: -5px 0;
        border-radius: 9px;
    }
""")
#TRACKING FOR VOLUME SLIDER/ICON
is_muted = False  # Flag to track mute state
previous_volume = 40  # Variable to store previous volume

# Function to apply volume using a logarithmic conversion
def apply_volume(value):
    global is_muted
    if is_muted and value > 0:  # If muted but slider is adjusted
        is_muted = False  # Reset the mute flag
    # Convert the slider value (0-100) to a logarithmic volume (0.0 to 1.0)
    if value == 0:
        linear_volume = 0.0
    else:
        linear_volume = math.pow(value / 100.0, 2)  # Logarithmic curve

    audio_output.setVolume(linear_volume)

apply_volume(volume_slider.value())
volume_slider.valueChanged.connect(apply_volume)

#VOLUME ICON
volume_icon = QPushButton(window)
volume_icon.setIcon(QIcon("sound_partial.png"))  # Replace with your icon file path
volume_icon.setStyleSheet("background-color: transparent; border: none;")
volume_icon.setGeometry(volume_slider.x() - 50, volume_slider.y() - 10, 40, 40)
volume_icon.setIconSize(QSize(35, 35))


def auto_mute(volume):
    if not is_muted:  # Only change icon if not manually muted
        if volume == 0:
            volume_icon.setIcon(QIcon("sound_off.png"))
        elif 1 <= volume < 75:
            volume_icon.setIcon(QIcon("sound_partial.png"))
        elif volume >= 75:
            volume_icon.setIcon(QIcon("sound_full.png"))


def volume_click():
    global is_muted, previous_volume
    if is_muted:
        volume_slider.setValue(previous_volume)  # Restore previous volume
        is_muted = False
        auto_mute(volume_slider.value())
    else:
        previous_volume = volume_slider.value()  # Store current volume
        volume_slider.setValue(0)  # Mute volume
        is_muted = True
        volume_icon.setIcon(QIcon("sound_muted.png"))


volume_slider.valueChanged.connect(auto_mute)
volume_icon.clicked.connect(volume_click)


window.show()
sys.exit(app.exec())
