
from Connection import SheetConnection

"""
Class that should inherit to all
types of words in a sentence
"""

class Worte:

    def __init__(self, sheet = "Nomen"):
        # I know, there is no way to change usecase
        self.connection = SheetConnection(sheet)

    def randomlySelect(self):
        # return diccionary
        pass

    def getUbersetzung(self):
        