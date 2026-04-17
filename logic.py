from gui import *
from PyQt6.QtWidgets import *

class Logic(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.label_Feedback.setText("")
        self.button_Save.clicked.connect(lambda : self.save())
        
    def save(self):
        
        character_name = self.input_Name.text().strip() if len(self.input_Name.text().strip()) > 0 else ""
        if character_name == "":
            QMessageBox.critical(self, "Error", "Please enter a character name.") #auto fill recommended this and i liked it
            self.label_Feedback.setText("Please enter a character name.")
            self.label_Feedback.setStyleSheet("color: red;")
            return
        
        elif ["/", "\\", "|", ":", "*"] in character_name:
            QMessageBox.critical(self, "Error", "Character name cannot contain special characters.")
            self.label_Feedback.setText("Character name cannot contain special characters.")
            self.label_Feedback.setStyleSheet("color: red;")
            return
        
        
        
            