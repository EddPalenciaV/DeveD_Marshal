import sys
from Revisionator import remove_revision_tags, tag_drawings
from pdf_Organiser import supersede_drawings, set_SS_directory, is_currentDirectory
from Transmit_Auto1000 import Save_as_PDF
from io import StringIO
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMainWindow, QDialog, QTextEdit, QInputDialog, QMessageBox, QSplashScreen
from PySide6.QtGui import QPixmap, QFont, QColor
from PySide6.QtCore import Qt, QTimer

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

        self.setWindowTitle("MarshalleDD")
        self.setFixedSize(300, 300)
        # Set window background color
        self.setStyleSheet("background-color: #333333;")        

        self.labelTop = QLabel("DeveD\nMarshalleDD - Sort, Tag and Report Drawings")
        self.labelTop.setAlignment(Qt.AlignCenter)

        self.labelBottom = QLabel("Created by Edd Palencia-Vanegas - January 2026\nVersion 1.0 - 22/01/2026")
        
        self.button_Marshalledd = QPushButton("MarshalleDD")
        self.button_Marshalledd.setFixedSize(280, 60)  # Width, Height
        self.button_Marshalledd.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border: 2px solid #2E7D32;
                border-radius: 6px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #1b5e20;
            }
        """)
        self.button_Marshalledd.clicked.connect(self.MarshalleDD)  

        self.button_Supersede_Drawings = QPushButton("1. Supersede Drawings")
        self.button_Supersede_Drawings.clicked.connect(self.pdf_Superseder)

        self.button_Revisionator = QPushButton("2. Fix Revision Tags")
        self.button_Revisionator.clicked.connect(self.Revision_Fix)

        self.button_Transmittal = QPushButton("3. Generate Transmittal PDF")
        self.button_Transmittal.clicked.connect(self.Transmittal_PDF)

        layout = QVBoxLayout() # Vertical Box Layout
        layout.addWidget(self.labelTop)
        layout.addWidget(self.button_Marshalledd)
        layout.addSpacing(15)        
        layout.addWidget(self.button_Supersede_Drawings)
        layout.addWidget(self.button_Revisionator)
        layout.addWidget(self.button_Transmittal)
        window = QWidget()
        window.setLayout(layout)

        self.setCentralWidget(window)

        # Create output dialog as instance variable
        self.output_dialog = OutputDialog(self)

    def MarshalleDD(self):
        # Clear previous output
        self.output_dialog.text_edit.clear()
        
        # Redirect stdout to the dialog
        sys.stdout = OutputCapture(self.output_dialog.text_edit)

        # Pattern that identifies a civil drawing
        civil_Pattern = r'-C-'
        # Pattern that identifies a architectural drawing
        arch_Pattern = r'-A-'
        # Pattern that identifies a structural drawing
        struct_Pattern = r'-S-'

        try:
            supersede_drawings(civil_Pattern, set_SS_directory(""))
            supersede_drawings(arch_Pattern, set_SS_directory(""))
            supersede_drawings(struct_Pattern, set_SS_directory(""))

            remove_revision_tags()
            tag_drawings()            

            Save_as_PDF(parent_window=self)
        finally:
            # Restore stdout
            sys.stdout = sys.__stdout__
            
            # Show the dialog with all accumulated text
            self.output_dialog.exec()

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

    def Revision_Fix(self):
        # Clear previous output
        self.output_dialog.text_edit.clear()
        
        # Redirect stdout to the dialog
        sys.stdout = OutputCapture(self.output_dialog.text_edit)

        try:
            remove_revision_tags()
            tag_drawings()
        finally:
            # Restore stdout
            sys.stdout = sys.__stdout__
            
            # Show the dialog with all accumulated text
            self.output_dialog.exec()

    def pdf_Superseder(self):
        # Clear previous output
        self.output_dialog.text_edit.clear()
        
        # Redirect stdout to the dialog
        sys.stdout = OutputCapture(self.output_dialog.text_edit)

        # Pattern that identifies a civil drawing
        civil_Pattern = r'-C-'
        # Pattern that identifies a architectural drawing
        arch_Pattern = r'-A-'
        # Pattern that identifies a structural drawing
        struct_Pattern = r'-S-'

        try:
            while True:
                # Print the menu options
                items = ["1. All together in _SS", "2. By Department"]
                # Prompt for user input
                choice, ok = QInputDialog.getItem(
                    self,
                    "Select Supersede Option",
                    "Choose from dropdown menu:",
                    items,
                    0,
                    False
                )

                if not ok:  # User clicked Cancel
                    print("Supersede selection cancelled.")
                    return None

                # Extract the number from the choice
                choice = choice[0]  
                # Activate choice
                if choice == '1':
                    supersede_drawings(civil_Pattern, set_SS_directory(""))
                    supersede_drawings(arch_Pattern, set_SS_directory(""))
                    supersede_drawings(struct_Pattern, set_SS_directory(""))
                    break
                elif choice == '2':
                    supersede_drawings(civil_Pattern, set_SS_directory("CIVIL"))
                    supersede_drawings(arch_Pattern, set_SS_directory("ARCHITECTURAL"))
                    supersede_drawings(struct_Pattern, set_SS_directory("STRUCTURAL"))
                    break                
                else:
                    QMessageBox.warning(self, "Invalid choice. Please enter a number between 1 and 3.")
                    continue
        finally:
            # Restore stdout
            sys.stdout = sys.__stdout__
            
            # Show the dialog with all accumulated text
            self.output_dialog.exec()

def show_splash_screen(app):
    """Display a splash screen with custom image"""
    # Load DeveD Logo
    pixmap = QPixmap("C:\\Users\\eddpa\\Desktop\\DeveD_Marshal\\MarshaleDD_small001.png")
    
    splash = QSplashScreen(pixmap)
    splash.setWindowFlags(splash.windowFlags() | Qt.WindowStaysOnTopHint)
    splash.show()
    
    splash.showMessage("Loading MarshalleDD v1.0...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
    
    app.processEvents()
    return splash

if __name__ == "__main__":     
    app = QApplication(sys.argv)
    splash = show_splash_screen(app)    
    window = MainWindow()
    window.show()
    # Show main window after 2000 milliseconds (2 seconds)
    QTimer.singleShot(1500, lambda: (window.show(), splash.finish(window)))
    app.exec()
    