
from Connection import SheetConnection

"""
Class that should inherit to all
types of words in a sentence
"""

class Worte:

    def __init__(self, sheet = "Nomen", columnName = "Wort"):
        # I know, there is no way to change usecase
        self.connection = SheetConnection(sheet)
        self.attributes = None
        self.ubersetzung = None
        self.randomly_Select(columnName)

    # returns DataFrame With 1 row
    def randomly_Select(self, desired_column:str):   
        # Select a word
        allRegisters = self.connection.getDataWithPandas()
        # https://www.geeksforgeeks.org/how-to-randomly-select-rows-from-pandas-dataframe/
        selectedRow = allRegisters.sample()

        self.attributes = self.define_Attributes(
                            allRegisters.keys().values,
                            selectedRow.values[0])
                            # We added [0], 'cause selectedRow is a bidimentional list

        # Filling the translations
        # In order for this to work, we shall always have
        # the german word we are looking for in the first 
        # Column 
        desiredWord = selectedRow.iat[0,0]
        
        # Searc for all the registers that have the same 
        # desiredWord
        unfilteredQuery = allRegisters.loc[allRegisters[desired_column] == desiredWord]
        
        # We filter, so we only get the differnt meanings
        self.ubersetzung = unfilteredQuery["Übersetzung"].values  
        
    def get_Ubersetzung(self):
        return self.ubersetzung

    def get_Attributes(self):
        return self.connection.getAttributes()
        
    def define_Attributes(self, attributes : list, values: list):
        mergedItems = []
        for i in range (len(attributes)): 
            mergedItems.append((attributes[i], values[i]))
        return dict(mergedItems)
    # Add a word