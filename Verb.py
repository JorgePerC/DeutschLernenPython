# Programa donde se encuentra la clase verbs

from Worte import Worte

class Verb (Worte):
    
    def __init__(self):
        Worte.__init__(self, "Verbs", "Verb")

    def conjugate(self, zeit: str, subjekt: str):
        if zeit == "präsens" or "gegenwart":
            return conjugate_in_present(subjekt)

    # It should be a good idea to create objekt Subject
    def conjugate_in_present(self, subjekt: str):
        if self.attributes["ist regelmäßige im Präsens"] == "TRUE":
            print("It's regular")
            # TODO: CHANGE IMPLEMENTAIION
            if subjekt == "ich":
                return self.changeEnding("e")
            elif subjekt == "du":
                return self.changeEnding("st")
            elif subjekt == "er":
                return self.changeEnding("t")
            elif subjekt == "wir":
                return self.attributes["Verb"]
            elif subjekt == "ihr":
                return self.changeEnding("t")
            elif subjekt == "sie":
                return self.attributes["Verb"]
        else:
            print("It's not regular")

    # Remove the last letters from the verb and 
    # place a new ending
    def changeEnding(self, ending: str):
        originalVerb = self.attributes["Verb"]
        modifiedVerb = originalVerb[:-2] 
        
        #TODO: MOVE!
        # This condition should not be here
            # if modifiedVerb[-1] == "d" or "t":
            #     modifiedVerb += "e" + ending
            # else:
            #     modifiedVerb += ending
        modifiedVerb += ending
        return modifiedVerb