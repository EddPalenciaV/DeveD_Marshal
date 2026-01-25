import sys
from Revisionator import remove_revision_tags, tag_drawings
from pdf_Organiser import supersede_drawings, set_SS_directory, is_currentDirectory
from Transmit_Auto1000 import Save_as_PDF
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMainWindow
from PyQt6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Marshal - Sort, Tag and Report Drawings")
        self.setFixedSize(QSize(300, 200))
        layout = QVBoxLayout() # Vertical Box Layout
        self.label = QLabel("DeveD - Marshal\nCreated by Edd Palencia-Vanegas - January 2026\nVersion 1.0 - 13/01/2026")
        self.button = QPushButton("Generate Transmittal PDF")
        self.button.clicked.connect(self.Transmittal_PDF)

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        window = QWidget()
        window.setLayout(layout)

        self.setCentralWidget(window)

    def Transmittal_PDF(self):
        Save_as_PDF()

def myApp():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__": 
    directory = is_currentDirectory()
    myApp()
    print("DeveD Marshal - Sort, Tag and Report Drawings")
    print("Created by Edd Palencia-Vanegas - January 2026. All rights reserved.")
    print("Version 1.0 - 22/01/2026")