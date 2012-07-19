import sys

from PySide.QtCore import *
from PySide.QtGui import *
import ConfigParser
import os

import ui_ItemChanger

class ItemChanger(QDialog, ui_ItemChanger.Ui_Dialog):
    def __init__(self, parent=None):
        self.DEEPER_DIRECTORY = "\\RADS\\solutions\\lol_game_client_sln\\releases\\0.0.0.26\\deploy\\DATA\\Characters"
        
        super(ItemChanger, self).__init__(parent)
        
        self.setupUi(self) # Calls the setupUi function which is built into the ui file.
        
        self.browseButton.clicked.connect(self.findLeague)
        self.saveButton.clicked.connect(self.saveItems)
        self.parser = ConfigParser.SafeConfigParser()
        
        # Giant dictionary of items.
        self.items = {3001 : 'Abyssal Scepter', 3105 : 'Aegis of the Legion', 1052 : 'Amplifying Tome', 3003 : "Archangel's Staff", 3174 : "Athene's Unholy Grail", 
                      3005 : "Atma's Impaler", 3196 : "Augment: Power", 3197 : "Augment: Gravity", 3198 : "Augment: Death", 3093 : "Avarice Blade", 1038 : "B.F. Sword", 
                      3102 : "Banshee's Veil", 3006 : "Berserker's Greaves", 3144 : "Bilgewater Cutlass", 3071 : "The Bloodthirster", 3117 : "Boots of Mobility", 
                      1001 : "Boots of Speed", 3009 : "Boots of Swiftness", 1051 : "Brawler's Gloves", 3134 : "The Brutalizer", 3010 : "Catalyst the Protector", 
                      1031 : "Chain Vest", 3028 : "Chalice of Harmony", 3172 : "Cloak and Dagger", 1018 : "Cloak of Agility", 1029 : "Cloth Armor", 1042 : "Dagger",
                      3128 : "Deathfire Grasp", 1055 : "Doran's Blade", 1056 : "Doran's Shield", 1054 : "Doran's Shield", 3173 : "Eleisa's Miracle", 2038 : "Elixir of Agility",
                      2039 : "Elixir of Brilliance", 2037 : "Elixir of Fortitude", 3097 : "Emblem of Valor", 3184 : "Entropy (Dominion only)", 3123 : "Executioner's Calling",
                      1004 : "Faerie Charm", 3108 : "Fiendish Codex", 3109 : "Force of Nature", 3110 : "Frozen Heart", 3022 : "Frozen Mallet", 1011 : "Giant's Belt",
                      3024 : "Glacial Shroud", 3026 : "Guardian Angel", 3124 : "Guinsoo's Rageblade", 3136 : "Haunting Guise", 2003 : "Health Potion", 3132 : "The Heart of Gold",
                      3200 : "The Hex Core", 3155 : "Hexdrinker", 3146 : "Hextech Gunblade", 3145 : "Hextech Revolver", 3187 : "Hextech Sweeper (Dominion Only)", 3031 : "Infinity Edge",
                      3158 : "Ionian Boots of Lucidity", 3178 : "Ionic Spark", 3098 : "Kage's Lucky Pick", 3067 : "Kindlegem", 3186 : "Kitae's Bloodrazor (Dominion only)",
                      3035 : "Last Whisper", 3138 : "Leviathan", 3100 : "Lich Bane", 3185 : "The Lightbringer", 3190 : "Locket of the Iron Solari", 1036 : "Long Sword",
                      3126 : "Madred's Bloodrazor", 3106 : "Madred's Razors", 3115 : "Malady", 3037 : "Mana Manipulator", 2004 : "Mana Potion", 3004 : "Manamune", 3156 : "Maw of Malmortius",
                      3041 : "Mejai's Soulstealer", 1005 : "Meki Pendant", 3111 : "Mercury's Treads", 3170 : "Moonflair Spellblade", 3165 : "Morello's Evil Tome", 3115 : "Nashor's Tooth",
                      1058 : "Needlessly Large Rod", 1057 : "Negatron Cloak", 3047 : "Ninja Tabi", 1033 : "Null-Magic Mantle", 3180 : "Odyn's Veil (Dominion Only)", 2042 : "Oracle's Elixir",
                      2047 : "Oracle's Extract (Dominion Only)", 3044 : "Phage", 3046 : "Phantom Dancer", 3096 : "Philosopher's Stone", 1037 : "Pickaxe",
                      1062 : "Prospector's Blade (Dominion Only)", 1063 : "Prospector's Ring", 3140 : "Quicksilver Sash", 3089 : "Rabadon's Deathcap", 3143 : "Randuin's Omen",
                      1043 : "Recurve Bow", 1007 : "Regrowth Pendant", 1006 : "Rejuvenation Bead", 3027 : "Rod of Ages", 1028 : "Ruby Crystal", 3116 : "Rylai's Crystal Scepter",
                      3181 : "Sanguine Blade (Dominion Only)", 1027 : "Saphire Crystal", 3057 : "Sheen", 3069 : "Shurelya's Reverie", 2044 : "Sight Ward", 3020 : "Sorcerer's Shoes",
                      3099 : "Soul Shroud", 3065 : "Spirit Visage", 3101 : "Stinger", 3068 : "Sunfire Cape", 3141 : "Sword of the Occult", 3070 : "Tear of the Goddess", 3075 : "Thornmail",
                      3077 : "Tiamat", 3078 : "Trinity Force", 1053 : "Vampiric Scepter", 2043 : "Vision Ward", 3135 : "Void Staff", 3082 : "Warden's Mail", 3083 : "Warmog's Armor", 
                      3152 : "Will of the Ancients", 3091 : "Wit's End", 3154 : "Wriggle's Lantern", 3142 : "Toumuu's Ghostblade", 3086 : "Zeal", 3050 : "Zeke's Herald", 
                      3157 : "Zhonya's Hourglass", 1056 : "Doran's Ring"}

        for key in self.items.values():
            self.oneBox.addItem(key)
            self.twoBox.addItem(key)
            self.threeBox.addItem(key)
            self.fourBox.addItem(key)
            self.fiveBox.addItem(key)
            self.sixBox.addItem(key)
            
            model = self.oneBox.model()
            model.sort(0)
            model = self.twoBox.model()
            model.sort(0)
            model = self.threeBox.model()
            model.sort(0)
            model = self.fourBox.model()
            model.sort(0)
            model = self.fiveBox.model()
            model.sort(0)
            model = self.sixBox.model()
            model.sort(0)
        self.updateUi()
        
        
        self.champBox.currentIndexChanged.connect(self.updateUi)
        try:
            file = open('config.ini', 'r+')
        except IOError:
            return
        self.parser.read(file.name)
        print self.parser.has_option('config', 'path')
        if self.parser.has_option('config', 'path'):
            self.pathEdit.setText(self.parser.get('config', 'path'))
        file.close()
        
    def updateUi(self):
        if not self.champBox.currentText() == "Champion":
            self.oneBox.setEnabled(True)
            self.twoBox.setEnabled(True)
            self.threeBox.setEnabled(True)
            self.fourBox.setEnabled(True)
            self.fiveBox.setEnabled(True)
            self.sixBox.setEnabled(True)
            try:
                if open(self.pathEdit.text() + "//" + self.champBox.currentText() + "//RecItemsCLASSIC.ini", 'r'):
                    champconfig = open(self.pathEdit.text() + "//" + self.champBox.currentText() + "//RecItemsCLASSIC.ini", 'r')
                    
                    self.parser.read(champconfig.name)
                                
                    item1number = self.parser.getint('ItemSet1', 'RecItem1')
                    item1 = self.items.get(item1number)
                    index = self.oneBox.findText(item1)
                    self.oneBox.setCurrentIndex(index)
                    
                    item2number = self.parser.getint('ItemSet1', 'RecItem2')
                    item2 = self.items.get(item2number)
                    index = self.twoBox.findText(item2)
                    self.twoBox.setCurrentIndex(index)
                    
                    item3number = self.parser.getint('ItemSet1', 'RecItem3')
                    item3 = self.items.get(item3number)
                    index = self.threeBox.findText(item3)
                    self.threeBox.setCurrentIndex(index)
                    
                    item4number = self.parser.getint('ItemSet1', 'RecItem4')
                    item4 = self.items.get(item4number)
                    index = self.fourBox.findText(item4)
                    self.fourBox.setCurrentIndex(index)
                    
                    item5number = self.parser.getint('ItemSet1', 'RecItem5')
                    item5 = self.items.get(item5number)
                    index = self.fiveBox.findText(item5)
                    self.fiveBox.setCurrentIndex(index)
                    
                    item6number = self.parser.getint('ItemSet1', 'RecItem6')
                    item6 = self.items.get(item6number)
                    index = self.sixBox.findText(item6)
                    self.sixBox.setCurrentIndex(index)
                    
                    champconfig.close()
                else:
                    self.oneBox.setEnabled(False)
                    self.twoBox.setEnabled(False)
                    self.threeBox.setEnabled(False)
                    self.fourBox.setEnabled(False)
                    self.fiveBox.setEnabled(False)
                    self.sixBox.setEnabled(False)
            except IOError:
                self.oneBox.setCurrentIndex(0)
                self.twoBox.setCurrentIndex(0)
                self.threeBox.setCurrentIndex(0)
                self.fourBox.setCurrentIndex(0)
                self.fiveBox.setCurrentIndex(0)
                self.sixBox.setCurrentIndex(0)
            
    def findLeague(self):
        path = QFileDialog.getExistingDirectory(self, 'Select League Directory (Containing the RADS folder) or Characters directory')
        self.path = QDir(path)
        
        if self.path.dirName() == 'League of Legends':
            self.path = QDir(path + "\\RADS\\solutions\\lol_game_client_sln\\releases\\0.0.0.165\\deploy\\DATA\\characters")
        elif self.path.dirName == 'characters':
            self.path = QDir(path)
        self.pathEdit.setText(self.path.absolutePath())
        file = open('config.ini', 'w')
        self.parser.read(file.name)
        if self.path.exists():
            if not self.parser.has_section('config'):
                self.parser.add_section('config')
            self.parser.set('config', 'path', self.path.absolutePath())
            self.parser.write(file)
            file.close()
            return
        else:
            self.pathEdit.setText("Path to League Client")
            QMessageBox.warning(self, "Incorrect Directory", "You must select the League of Legends folder \n(it should contain a 'RADS' subdirectory)")
            file.close()
            return

    def saveItems(self):
        inifile = self.pathEdit.text() + "//" + self.champBox.currentText() + "//RecItemsCLASSIC.ini"
        
        if not os.path.exists(self.pathEdit.text() + "//" + self.champBox.currentText()):
            os.makedirs(self.pathEdit.text() + "//" + self.champBox.currentText())
        
        file = open(inifile, 'w')
        
        self.parser.read(file.name)
        
        if self.parser.has_section('ItemSet1'):
            self.parser.set('ItemSet1', 'SetName', 'Set1')
            for id, item in self.items.items():
                if item == self.oneBox.currentText():
                    item1 = id
                if item == self.twoBox.currentText():
                    item2 = id 
                if item == self.threeBox.currentText():
                    item3 = id
                if item == self.fourBox.currentText():
                    item4 = id
                if item == self.fiveBox.currentText():
                    item5 = id
                if item == self.sixBox.currentText():
                    item6 = id
            
            if "Item" in self.oneBox.currentText():
                QMessageBox.warning(self, "Incomplete Form", "Not all of the items have been selected! \nPlease select all 6 items.")
                return
            if "Item" in self.twoBox.currentText():
                QMessageBox.warning(self, "Incomplete Form", "Not all of the items have been selected! \nPlease select all 6 items.")
                return
            if "Item" in self.threeBox.currentText():
                QMessageBox.warning(self, "Incomplete Form", "Not all of the items have been selected! \nPlease select all 6 items.")
                return
            if "Item" in self.fourBox.currentText():
                QMessageBox.warning(self, "Incomplete Form", "Not all of the items have been selected! \nPlease select all 6 items.")
                return
            if "Item" in self.fiveBox.currentText():
                QMessageBox.warning(self, "Incomplete Form", "Not all of the items have been selected! \nPlease select all 6 items.")
                return
            if "Item" in self.sixBox.currentText():
                QMessageBox.warning(self, "Incomplete Form", "Not all of the items have been selected! \nPlease select all 6 items.")
                return
            
            self.parser.set('ItemSet1', 'RecItem1', str(item1))
            self.parser.set('ItemSet1', 'RecItem2', str(item2))
            self.parser.set('ItemSet1', 'RecItem3', str(item3))
            self.parser.set('ItemSet1', 'RecItem4', str(item4))
            self.parser.set('ItemSet1', 'RecItem5', str(item5))
            self.parser.set('ItemSet1', 'RecItem6', str(item6))
            
            self.parser.remove_section('config')
            
            self.parser.write(file)
            file.close()
            QMessageBox.information(self, "Complete", "Your file was saved successfully.")
        else:
            self.parser.add_section('ItemSet1')
            file.close()
            self.saveItems()
            
def main():
    app = QApplication(sys.argv)
    form = ItemChanger()
    form.show()
    app.exec_()
    
main()