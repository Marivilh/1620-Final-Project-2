from gui import *
import json
from PyQt6.QtWidgets import *

class Logic(QMainWindow, Ui_mainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        self.label_Feedback.setText("")
        self.tabWidget.setCurrentIndex(0)
        self.input_Name.setFocus()
        # load the buttons
        self.button_Save.clicked.connect(lambda : self.save())
        self.button_Reset.clicked.connect(lambda : self.reset())
        self.button_Load.clicked.connect(lambda : self.load_json())
        
        #update the modifier labels and skills when the attribute scores are changed
        self.choose_STR.currentTextChanged.connect(lambda : self.update_modifiers())
        self.choose_DEX.currentTextChanged.connect(lambda : self.update_modifiers())
        self.choose_CON.currentTextChanged.connect(lambda : self.update_modifiers())
        self.choose_INT.currentTextChanged.connect(lambda : self.update_modifiers())
        self.choose_WIS.currentTextChanged.connect(lambda : self.update_modifiers())
        self.choose_CHA.currentTextChanged.connect(lambda : self.update_modifiers())
          
    def update_modifiers(self) -> None:
        """
        updates the modifiers for the attributes and skills
        """
        # update the feedback label
        self.label_Feedback.setText("Core Stats Updated. Re-apply any proficiencies to the Skills Tab.")
        self.label_Feedback.setStyleSheet("color: orange;")
        
        bonuses = {}
        str_bonus = (int(self.choose_STR.currentText()) - 10) // 2
        bonuses["STR"] = str_bonus
        dex_bonus = (int(self.choose_DEX.currentText()) - 10) // 2
        bonuses["DEX"] = dex_bonus
        con_bonus = (int(self.choose_CON.currentText()) - 10) // 2
        bonuses["CON"] = con_bonus
        int_bonus = (int(self.choose_INT.currentText()) - 10) // 2
        bonuses["INT"] = int_bonus
        wis_bonus = (int(self.choose_WIS.currentText()) - 10) // 2
        bonuses["WIS"] = wis_bonus
        cha_bonus = (int(self.choose_CHA.currentText()) - 10) // 2
        bonuses["CHA"] = cha_bonus
        
        # update the labels in arttributes tab    
        for stat, bonus in bonuses.items():
            if stat == "STR":
                if bonus >= 0:
                    self.label_STR_Bonus.setText(f"(+{bonus})")
                elif bonus < 0:
                    self.label_STR_Bonus.setText(f"({bonus})")
                else:
                    self.label_STR_Bonus.setText("(+0)")
            elif stat == "DEX":
                if bonus >= 0:
                    self.label_DEX_Bonus.setText(f"(+{bonus})")
                elif bonus < 0:
                    self.label_DEX_Bonus.setText(f"({bonus})")
                else:
                    self.label_DEX_Bonus.setText("(+0)")
            elif stat == "CON":
                if bonus >= 0:
                    self.label_CON_Bonus.setText(f"(+{bonus})")
                elif bonus < 0:
                    self.label_CON_Bonus.setText(f"({bonus})")
                else:
                    self.label_CON_Bonus.setText("(+0)")
            elif stat == "INT":
                if bonus >= 0:
                    self.label_INT_Bonus.setText(f"(+{bonus})")
                elif bonus < 0:
                    self.label_INT_Bonus.setText(f"({bonus})")
                else:
                    self.label_INT_Bonus.setText("(+0)")
            elif stat == "WIS":
                if bonus >= 0:
                    self.label_WIS_Bonus.setText(f"(+{bonus})")
                elif bonus < 0:
                    self.label_WIS_Bonus.setText(f"({bonus})")
                else:
                    self.label_WIS_Bonus.setText("(+0)")
            elif stat == "CHA":
                if bonus >= 0:
                    self.label_CHA_Bonus.setText(f"(+{bonus})")
                elif bonus < 0:
                    self.label_CHA_Bonus.setText(f"({bonus})")
                else:
                    self.label_CHA_Bonus.setText("(+0)")
                    
        # update the saving throw modifiers
        self.choose_STR_mod.setValue(str_bonus)
        self.choose_DEX_mod.setValue(dex_bonus)
        self.choose_CON_mod.setValue(con_bonus)
        self.choose_INT_mod.setValue(int_bonus)
        self.choose_WIS_mod.setValue(wis_bonus)
        self.choose_CHA_mod.setValue(cha_bonus)
        
        # update the skill modifiers
        self.choose_Acrobatics.setValue(dex_bonus)
        self.choose_Animal_Handling.setValue(wis_bonus)
        self.choose_Arcana.setValue(int_bonus)
        self.choose_Athletics.setValue(str_bonus)
        self.choose_Deception.setValue(cha_bonus)
        self.choose_History.setValue(int_bonus)
        self.choose_Insight.setValue(wis_bonus)
        self.choose_Intimidation.setValue(cha_bonus)
        self.choose_Investigation.setValue(int_bonus)
        self.choose_Medicine.setValue(wis_bonus)
        self.choose_Nature.setValue(int_bonus)
        self.choose_Perception.setValue(wis_bonus)
        self.choose_Performance.setValue(cha_bonus)
        self.choose_Persuasion.setValue(cha_bonus)
        self.choose_Religion.setValue(int_bonus)
        self.choose_Sleight_of_Hand.setValue(dex_bonus)
        self.choose_Stealth.setValue(dex_bonus)
        self.choose_Survival.setValue(wis_bonus)

    def reset(self) -> None:
        """
        resets everything back to default
        """
        #resets ALL the fields to default
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

            #reset all in Attributes Tab
            self.choose_Class.setCurrentIndex(0)
            self.choose_Alignment.setCurrentIndex(0)
            self.choose_Level.setCurrentIndex(0)
            self.choose_STR.setCurrentIndex(9)
            self.choose_DEX.setCurrentIndex(9)
            self.choose_CON.setCurrentIndex(9)
            self.choose_INT.setCurrentIndex(9)
            self.choose_WIS.setCurrentIndex(9)
            self.choose_CHA.setCurrentIndex(9)
            self.choose_AC.setValue(1)
            self.choose_Initiative.setValue(1)
            self.choose_Speed.setValue(30)
            self.choose_Hit_Points.setValue(1)
            self.choose_Hit_Dice.setValue(1)
            self.label_STR_Bonus.setText("(+0)")
            self.label_DEX_Bonus.setText("(+0)")
            self.label_CON_Bonus.setText("(+0)")
            self.label_INT_Bonus.setText("(+0)")
            self.label_WIS_Bonus.setText("(+0)")
            self.label_CHA_Bonus.setText("(+0)")
            
            #reset all in Skills Tab
            self.choose_STR_mod.setValue(0)
            self.choose_DEX_mod.setValue(0)
            self.choose_CON_mod.setValue(0)
            self.choose_INT_mod.setValue(0)
            self.choose_WIS_mod.setValue(0)
            self.choose_CHA_mod.setValue(0)
            self.choose_Acrobatics.setValue(0)
            self.choose_Animal_Handling.setValue(0)
            self.choose_Arcana.setValue(0)
            self.choose_Athletics.setValue(0)
            self.choose_Deception.setValue(0)
            self.choose_History.setValue(0)
            self.choose_Insight.setValue(0)
            self.choose_Intimidation.setValue(0)
            self.choose_Investigation.setValue(0)
            self.choose_Medicine.setValue(0)
            self.choose_Nature.setValue(0)
            self.choose_Perception.setValue(0)
            self.choose_Performance.setValue(0)
            self.choose_Persuasion.setValue(0)
            self.choose_Religion.setValue(0)
            self.choose_Sleight_of_Hand.setValue(0)
            self.choose_Stealth.setValue(0)
            self.choose_Survival.setValue(0)
            #reset all in Spells Tab
            self.choose_Spellcasting_Ability.setCurrentIndex(0)
            self.choose_Spell_Save_DC.setValue(0)
            self.choose_Spell_Attack_Bonus.setValue(0)
            
            #set focus back to name entry
            self.tabWidget.setCurrentIndex(0)
            self.input_Name.setFocus()
            
            #update the feedback label
            self.label_Feedback.setText("Character sheet reset to default.")
            self.label_Feedback.setStyleSheet("color: green;")
        
    def get_attributes(self) -> dict:
        """get
        gets the info from the Attributes tab and returns
        it as a dict.
        also cheks the validity of the chracters name
        """
        stats = {}
    
        character_name = self.input_Name.text().strip() if len(self.input_Name.text().strip()) > 0 else ""
        # check if the name is valid
        if character_name == "":
            QMessageBox.critical(self, "Error", "Please enter a character name.") #auto fill recommended this and i liked it
            self.label_Feedback.setText("Please enter a character name.")
            self.label_Feedback.setStyleSheet("color: red;")
            return
        # no weird characs in the name
        elif character_name in ["/", "\\", "|", ":", "*"]:
            QMessageBox.critical(self, "Error", "Character name cannot contain special characters.")
            self.label_Feedback.setText("Character name cannot contain special characters.")
            self.label_Feedback.setStyleSheet("color: red;")
            return
    
        else:
            #get the name, class, race, bg, alignment, and level
            stats["Name"] = character_name  
            stats["Class"] = self.choose_Class.currentText() if len(self.choose_Class.currentText()) > 0 else "None"
            stats["Race"] = self.input_Race.text().strip() if len(self.input_Race.text().strip()) > 0 else "None"
            stats["Background"] = self.input_Background.text().strip() if len(self.input_Background.text().strip()) > 0 else "None"
            stats["Alignment"] = self.choose_Alignment.currentText() if len(self.choose_Alignment.currentText()) > 0 else "None"
            stats["Level"] = self.choose_Level.currentText()
            
            #get the stats
            stats["Strength"] = self.choose_STR.currentText()
            stats["Dexterity"] = self.choose_DEX.currentText()
            stats["Constitution"] = self.choose_CON.currentText()
            stats["Intelligence"] = self.choose_INT.currentText()
            stats["Wisdom"] = self.choose_WIS.currentText()
            stats["Charisma"] = self.choose_CHA.currentText()
            
            return stats, character_name
            
    def get_skills(self) -> dict:
        """
        gets the info from the Skills tab 
        and returns it as a dict
        """
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
        """
        gets the info from the Proficiencies tab 
        and returns it as a dict
        """
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
        """
        gets the info from the Features tab 
        and returns it as a dict
        """
        features = {}
        # get the text in the box
        features["Features_and_Traits"] = self.input_Features_and_Traits.toPlainText().strip() if len(self.input_Features_and_Traits.toPlainText().strip()) > 0 else "None"
        
        return features

    def get_details(self) -> dict:
        """
        gets the info from the Details tab 
        and returns it as a dict
        """
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
        """
        gets the info from the Spells tab 
        and returns it as a dict
        """
        spells = {}
        # get the spellcasting class, ability, save dc, and atk bonus
        spells["Spellcasting_Class"] = self.input_Spellcasting_Class.text().strip() if len(self.input_Spellcasting_Class.text().strip()) > 0 else "None"
        spells["Spellcasting_Ability"] = self.choose_Spellcasting_Ability.currentText() if self.choose_Spellcasting_Ability.currentText() != "" else "None"
        spells["Spell_Save_DC"] = self.choose_Spell_Save_DC.value() if self.choose_Spell_Save_DC != "0" else "None"
        spells["Spell_Attack_Bonus"] = self.choose_Spell_Attack_Bonus.value() if self.choose_Spell_Attack_Bonus != "0" else "None"

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
        """
        saves all the info to a json file
        named after the character
        """
        all_stats = {}     
        data = self.get_attributes()   
        #check is atributes is not None
        if data is None:
            return
        
        stats, character_name = data
        if stats is not None and character_name is not None:            
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
            try:
                filen_name = f"{character_name}.json"
                with open(filen_name, "w") as f:
                    json.dump(all_stats, f, indent=4)
                QMessageBox.information(self, "Success", f"Character saved as {filen_name}.")
                self.label_Feedback.setText(f"Character saved as {filen_name}.")
                self.label_Feedback.setStyleSheet("color: green;")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred while saving the character: {str(e)}")
                self.label_Feedback.setText(f"An error occurred while saving the character: {str(e)}")
                self.label_Feedback.setStyleSheet("color: red;")

                
        def load_json(self) -> None:
            """
            loads a character from a json file
            and populates the fields with the data
            """
            pass
