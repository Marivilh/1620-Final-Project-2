from gui import *
import json
from PyQt6.QtWidgets import *

class Logic(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.label_Feedback.setText("")
        self.button_Save.clicked.connect(lambda : self.save())
        
    def save(self):
        stats = {}
        
        character_name = self.input_Name.text().strip() if len(self.input_Name.text().strip()) > 0 else ""
        # check if the name is valid
        if character_name == "":
            QMessageBox.critical(self, "Error", "Please enter a character name.") #auto fill recommended this and i liked it
            #self.label_Feedback.setText("Please enter a character name.")
            #self.label_Feedback.setStyleSheet("color: red;")
            return
        # no weird characs in the name
        elif character_name in ["/", "\\", "|", ":", "*"]:
            QMessageBox.critical(self, "Error", "Character name cannot contain special characters.")
            #self.label_Feedback.setText("Character name cannot contain special characters.")
            #self.label_Feedback.setStyleSheet("color: red;")
            return
        
        else:
            #get the name, class, race, bg, alignment, and level
            stats["name"] = character_name  
            stats["class"] = self.choose_Class.currentText()
            stats["race"] = self.input_Race.text().strip() if len(self.input_Race.text().strip()) > 0 else ""
            stats["background"] = self.input_Background.text().strip() if len(self.input_Background.text().strip()) > 0 else ""
            stats["alignment"] = self.choose_Alignment.currentText()
            stats["level"] = self.choose_Level.currentText()
            
            #get the stats
            stats["strength"] = self.choose_STR.currentText()
            stats["dexterity"] = self.choose_DEX.currentText()
            stats["constitution"] = self.choose_CON.currentText()
            stats["intelligence"] = self.choose_INT.currentText()
            stats["wisdom"] = self.choose_WIS.currentText()
            stats["charisma"] = self.choose_CHA.currentText()
            
            print(stats)
            #saves the info from stats to the json
            try:
                filen_name = f"{character_name}.json"
                with open(filen_name, "w") as f:
                    json.dump(stats, f, indent=4)
                QMessageBox.information(self, "Success", f"Character saved as {filen_name}.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred while saving the character: {str(e)}")
                

