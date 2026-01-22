import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

def myApp():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Marshal - Sort, Tag and Report Drawings")
    layout = QVBoxLayout(window)

    label = QLabel("DeveD - Marshal\nCreated by Edd Palencia-Vanegas - January 2026\nVersion 1.0 - 13/01/2026", parent=window)
    button = QPushButton("Generate Transmittal PDF", parent=window)

    layout.addWidget(label)
    layout.addWidget(button)

    window.show()

    app.exec()

if __name__ == "__main__": 
    myApp()
    print("DeveD Marshal - Sort, Tag and Report Drawings")
    print("Created by Edd Palencia-Vanegas - January 2026. All rights reserved.")
    print("Version 1.0 - 22/01/2026")