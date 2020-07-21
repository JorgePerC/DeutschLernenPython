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
        self.Worte = Worte (self, "Nomen")

        #Actual noun
        self.wort = self.Worte.selectedRow["Wort"]
        #Article
        self.artikel = self.Worte.selectedRow["Artikel"]
        #Noun in plural form
        self.plural = self.Worte.selectedRow["Plural"] 
        #Classification 
        self.einstufung = self.Worte.selectedRow["Einstufung"]