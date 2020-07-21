
from Connection import SheetConnection

"""
Class that should inherit to all
types of words in a sentence
"""

class Worte:

    def __init__(self, sheet = "Nomen"):
        # I know, there is no way to change usecase
        self.connection = SheetConnection(sheet)
        self.selectedRow = None
        self.ubersetzung = None
        self.randomly_Select()

    # returns DataFrame With 1 row
    def randomly_Select(self):   
        # Select a word
        allRegisters = self.connection.getDataWithPandas()
        # https://www.geeksforgeeks.org/how-to-randomly-select-rows-from-pandas-dataframe/
        self.selectedRow = allRegisters.sample()

        # Filling the translations
        # In order for this to work, we shall always have
        # the german word we are looking for in the first 
        # Column 
        desiredWord = self.selectedRow.iat[0,0]
        
        # TODO : Make "Wort" Variable
        unfilteredQuery = allRegisters.loc[allRegisters["Wort"] == desiredWord]
        
        self.ubersetzung = unfilteredQuery["Übersetzung"].values  
        
    def getUbersetzung(self):
        return self.ubersetzung

    def get_Attributes(self):
        return self.connection.getAttributes()
        