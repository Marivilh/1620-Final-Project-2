from gui import *
import json
from PyQt6.QtWidgets import *

class Logic(QMainWindow, Ui_mainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        self.label_Feedback.setText("")
        self.button_Save.clicked.connect(lambda : self.save())
        self.button_Reset.clicked.connect(lambda : self.reset())
        
    def reset(self) -> None:
        #resets ALL the fields to default
        #TODO: reset everything after a confirmation message
        confirm = QMessageBox.question(self, "Confirm Reset", "Are you sure you want to reset the character sheet? All unsaved data will be lost.", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.Yes:
            # reset all the text fields
            self.input_Name.setText("")
            self.input_Race.setText("")
            self.input_Background.setText("")
            self.input_Armor_Prof.setText("")
            self.input_Weapons_Prof.setText("")
            self.input_Tools_Prof.setText("")
            self.input_Language_Prof.setText("")
            self.input_Other_Profs.setText("")
            self.input_Equipment.setPlainText("")
            self.input_Features_and_Traits.setPlainText("")
            self.input_Character_Backstory.setPlainText("")
            self.input_Treasure.setPlainText("")
            self.input_Allies.setPlainText("")
            self.input_Extra_Features.setPlainText("")
            self.input_Age.setText("")
            self.input_Height.setText("")
            self.input_Weight.setText("")
            self.input_Eyes.setText("")
            self.input_Skin.setText("")
            self.input_Hair.setText("")
            self.input_Spellcasting_Class.setText("")
            self.input_Cantrips.setPlainText("# of Spell Slots\n(Spells)")
            self.input_Level_1_Spells.setPlainText("# of Spell Slots\n(Spells)")
            self.input_Level_2_Spells.setPlainText("# of Spell Slots\n(Spells)")
            self.input_Level_3_Spells.setPlainText("# of Spell Slots\n(Spells)")
            self.input_Level_4_Spells.setPlainText("# of Spell Slots\n(Spells)")
            self.input_Level_5_Spells.setPlainText("# of Spell Slots\n(Spells)")
            self.input_Level_6_Spells.setPlainText("# of Spell Slots\n(Spells)")
            self.input_Level_7_Spells.setPlainText("# of Spell Slots\n(Spells)")
            self.input_Level_8_Spells.setPlainText("# of Spell Slots\n(Spells)")
            self.input_Level_9_Spells.setPlainText("# of Spell Slots\n(Spells)")
            
            #TODO: reset the rest
        
    def get_attributes(self) -> dict:
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
            
            return stats, character_name
            
    def get_skills(self) -> dict:
        #TODO: get the skills and proficiencies
        # get the saving throws
        skills = {}
        skills["STR_save"] = self.choose_STR_mod.value()
        skills["DEX_save"] = self.choose_DEX_mod.value()
        skills["CON_save"] = self.choose_CON_mod.value()
        skills["INT_save"] = self.choose_INT_mod.value()
        skills["WIS_save"] = self.choose_WIS_mod.value()
        skills["CHA_save"] = self.choose_CHA_mod.value()
        
        #get skill throws
        skills["Acrobatics"] = self.choose_Acrobatics.value()
        skills["Animal_Handling"] = self.choose_Animal_Handling.value()
        skills["Arcana"] = self.choose_Arcana.value()
        skills["Athletics"] = self.choose_Athletics.value()
        skills["Deception"] = self.choose_Deception.value()
        skills["History"] = self.choose_History.value()
        skills["Insight"] = self.choose_Insight.value()
        skills["Intimidation"] = self.choose_Intimidation.value()
        skills["Investigation"] = self.choose_Investigation.value()
        skills["Medicine"] = self.choose_Medicine.value()
        skills["Nature"] = self.choose_Nature.value()
        skills["Perception"] = self.choose_Perception.value()
        skills["Performance"] = self.choose_Performance.value()
        skills["Persuasion"] = self.choose_Persuasion.value()
        skills["Religion"] = self.choose_Religion.value()
        skills["Sleight_of_Hand"] = self.choose_Sleight_of_Hand.value()
        skills["Stealth"] = self.choose_Stealth.value()
        skills["Survival"] = self.choose_Survival.value()
        
        return skills
    
    def get_proficiencies(self) -> dict:
        #TODO: i dont think this one is needed (check over the stat sheet structure)
        # nvm im dumb and this is needed
        # get the proficiencies & equipemnt
        proficiencies = {}
        proficiencies["Armor"] = self.input_Armor_Prof.text().strip() if len(self.input_Armor_Prof.text().strip()) > 0 else "None"
        proficiencies["Weapons"] = self.input_Weapons_Prof.text().strip() if len(self.input_Weapons_Prof.text().strip()) > 0 else "None"
        proficiencies["Tools"] = self.input_Tools_Prof.text().strip() if len(self.input_Tools_Prof.text().strip()) > 0 else "None"
        proficiencies["Languages"] = self.input_Language_Prof.text().strip() if len(self.input_Language_Prof.text().strip()) > 0 else "None"
        proficiencies["Other"] = self.input_Other_Profs.text().strip() if len(self.input_Other_Profs.text().strip()) > 0 else "None"
        # get equipment
        proficiencies["Equipment"] = self.input_Equipment.toPlainText().strip() if len(self.input_Equipment.toPlainText().strip()) > 0 else "None"
    
        return proficiencies
    
    def get_features(self) -> dict:
        #TODO: get the features and traits
        features = {}
        # get the text in the box
        features["Features_and_Traits"] = self.input_Features_and_Traits.toPlainText().strip() if len(self.input_Features_and_Traits.toPlainText().strip()) > 0 else "None"
        
        return features

    def get_details(self) -> dict:
        #TODO: get details (age, height, weight, eyes, skin, hair, and detailed background)
        details = {}
        # get the physical deets
        details["Age"] = self.input_Age.text().strip() if len(self.input_Age.text().strip()) > 0 else "None"
        details["Height"] = self.input_Height.text().strip() if len(self.input_Height.text().strip()) > 0 else "None"
        details["Weight"] = self.input_Weight.text().strip() if len(self.input_Weight.text().strip()) > 0 else "None"
        details["Eyes"] = self.input_Eyes.text().strip() if len(self.input_Eyes.text().strip()) > 0 else "None"
        details["Skin"] = self.input_Skin.text().strip() if len(self.input_Skin.text().strip()) > 0 else "None"
        details["Hair"] = self.input_Hair.text().strip() if len(self.input_Hair.text().strip()) > 0 else "None"
        
        # get the detailed background, treasure, allies, and any extra features
        details["Detailed_Background"] = self.input_Character_Backstory.toPlainText().strip() if len(self.input_Character_Backstory.toPlainText().strip()) > 0 else "None"
        details["Treasure"] = self.input_Treasure.toPlainText().strip() if len(self.input_Treasure.toPlainText().strip()) > 0 else "None"
        details["Allies"] = self.input_Allies.toPlainText().strip() if len(self.input_Allies.toPlainText().strip()) > 0 else "None"
        details["Extra_Features"] = self.input_Extra_Features.toPlainText().strip() if len(self.input_Extra_Features.toPlainText().strip()) > 0 else "None"
        
        return details

    def get_spells(self) -> dict:
        #TODO: get spells (if any)
        spells = {}
        # get the spellcasting class, ability, save dc, and atk bonus
        spells["Spellcasting_Class"] = self.input_Spellcasting_Class.text().strip() if len(self.input_Spellcasting_Class.text().strip()) > 0 else "None"
        spells["Spellcasting_Ability"] = self.choose_Spellcasting_Ability.currentText() if self.input_Spellcasting_Class.text().strip() != "" else "None"
        spells["Spell_Save_DC"] = self.choose_Spell_Save_DC.value() if self.input_Spellcasting_Class.text().strip() != "0" else "None"
        spells["Spell_Attack_Bonus"] = self.choose_Spell_Attack_Bonus.value() if self.input_Spellcasting_Class.text().strip() != "0" else "None"
        
        # get the actuall spells now
        default_spell_text = "# of Spell Slots\n(Spells)"
        spells["Cantrips"] = self.input_Cantrips.toPlainText().strip() if len(self.input_Cantrips.toPlainText().strip()) > 0 and self.input_Cantrips.toPlainText().strip() != default_spell_text else "None"
        spells["Level_1_Spells"] = self.input_Level_1_Spells.toPlainText().strip() if len(self.input_Level_1_Spells.toPlainText().strip()) > 0 and self.input_Level_1_Spells.toPlainText().strip() != default_spell_text else "None"
        spells["Level_2_Spells"] = self.input_Level_2_Spells.toPlainText().strip() if len(self.input_Level_2_Spells.toPlainText().strip()) > 0 and self.input_Level_2_Spells.toPlainText().strip() != default_spell_text else "None"
        spells["Level_3_Spells"] = self.input_Level_3_Spells.toPlainText().strip() if len(self.input_Level_3_Spells.toPlainText().strip()) > 0 and self.input_Level_3_Spells.toPlainText().strip() != default_spell_text else "None"
        spells["Level_4_Spells"] = self.input_Level_4_Spells.toPlainText().strip() if len(self.input_Level_4_Spells.toPlainText().strip()) > 0 and self.input_Level_4_Spells.toPlainText().strip() != default_spell_text else "None"
        spells["Level_5_Spells"] = self.input_Level_5_Spells.toPlainText().strip() if len(self.input_Level_5_Spells.toPlainText().strip()) > 0 and self.input_Level_5_Spells.toPlainText().strip() != default_spell_text else "None"
        spells["Level_6_Spells"] = self.input_Level_6_Spells.toPlainText().strip() if len(self.input_Level_6_Spells.toPlainText().strip()) > 0 and self.input_Level_6_Spells.toPlainText().strip() != default_spell_text else "None"
        spells["Level_7_Spells"] = self.input_Level_7_Spells.toPlainText().strip() if len(self.input_Level_7_Spells.toPlainText().strip()) > 0 and self.input_Level_7_Spells.toPlainText().strip() != default_spell_text else "None"
        spells["Level_8_Spells"] = self.input_Level_8_Spells.toPlainText().strip() if len(self.input_Level_8_Spells.toPlainText().strip()) > 0 and self.input_Level_8_Spells.toPlainText().strip() != default_spell_text else "None"
        spells["Level_9_Spells"] = self.input_Level_9_Spells.toPlainText().strip() if len(self.input_Level_9_Spells.toPlainText().strip()) > 0 and self.input_Level_9_Spells.toPlainText().strip() != default_spell_text else "None"
        
        return spells

    def save(self) -> None:
        #saves the info from stats to the json
        all_stats = {}
        
        stats, character_name = self.get_attributes()
        skills = self.get_skills()
        proficiencies = self.get_proficiencies()
        features = self.get_features()
        details = self.get_details()
        spells = self.get_spells()
        
        all_stats["Attributes"] = stats
        all_stats["Skills"] = skills
        all_stats["Proficiencies"] = proficiencies
        all_stats["Features"] = features
        all_stats["Details"] = details
        all_stats["Spells"] = spells
        
        if stats is not None:
            try:
                filen_name = f"{character_name}.json"
                with open(filen_name, "w") as f:
                    json.dump(all_stats, f, indent=4)
                QMessageBox.information(self, "Success", f"Character saved as {filen_name}.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred while saving the character: {str(e)}")
                

