import sys
from Revisionator import remove_revision_tags, tag_drawings
from pdf_Organiser import supersede_drawings, set_SS_directory, is_currentDirectory
from Transmit_Auto1000 import Save_as_PDF
from io import StringIO
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMainWindow, QDialog, QTextEdit
from PyQt6.QtCore import QSize

class OutputCapture(StringIO):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def write(self, text):
        super().write(text)
        self.text_widget.append(text.rstrip('\n'))

class OutputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Output")
        self.setGeometry(100, 100, 500, 400)
        
        layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        layout.addWidget(self.text_edit)
        
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MarshalleDD - Sort, Tag and Report Drawings")
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

        # Create output dialog as instance variable
        self.output_dialog = OutputDialog(self)

    def Transmittal_PDF(self):
        # Clear previous output
        self.output_dialog.text_edit.clear()
        
        # Redirect stdout to the dialog
        sys.stdout = OutputCapture(self.output_dialog.text_edit)

        try:
            Save_as_PDF(parent_window=self)
        finally:
            # Restore stdout
            sys.stdout = sys.__stdout__
            
            # Show the dialog with all accumulated text
            self.output_dialog.exec()


if __name__ == "__main__": 
    directory = is_currentDirectory()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    