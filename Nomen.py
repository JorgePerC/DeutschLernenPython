from Worte import Worte
import pandas as pd
"""
Code for object Nomen, sustantive in english.
Sorry for the variable names in german
but one must practice
"""

# https://www.geeksforgeeks.org/inheritance-in-python/
class Nomen (Worte):
    #Static variable for class Nomen
    # Show I make worte a static variable?
        # No, because each word changes
        # Yes, to avoid multuple connections -> therefore requests

    def __init__(self):

        # Do NOT CHANGE
        # Parent attributes and methods
        self.Worte = Worte.__init__(self, "Nomen")

        #Actual noun
        self.wort = self.selectedRow["Wort"].values
        #Article
        self.artikel = self.selectedRow["Artikel"].values
        #Noun in plural form
        self.plural = self.selectedRow["Plural"].values 
        #Classification 
        self.einstufung = self.selectedRow["Einstufung"].values