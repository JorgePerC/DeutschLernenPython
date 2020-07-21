from Connection import Connection
import pandas as pd
"""
Code for object Nomen, sustantive in english.
Sorry for the variable names in german
but one must practice
"""

class Nomen:
    #Static variable for class Nomen
    GSconnection = Connection()

    def __init__(self):
        
        
        #Article
        self.artikel
        #Actual noun
        self.wort
        #Noun in plural form
        self.plural
        #Classification 
        self.einstufung
