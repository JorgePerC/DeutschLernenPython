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
        self.Worte = Worte.__init__(self, "Nomen", "Wort")


class ArtikelPredicter:
    
    """
        Class to try to predict a Noun's genere
        If it has a [A], it means that the rule ALLWAYS applies
        If [U], USUALLY applies
        Rules that don't always apply, will be written in different 
        methods
    """
    
    def __init__(self):
        pass
    
    def isMaskulin(self, Nomen: str):
        
        #Is in days of the week
        #Is is Year seasons
        #Is in Monaten
        #Is in wheather
        #Is in times of the day
        #Cardinal places
        #Car makers
        #Trains
        #Alchoholic beberages
        
        # -ismus [A]
        # -ner [A]

        # -er [U]
        # -ling [U]
        # -or [U]
        # -ist [U]
        
        
        if Nomen[-3:] == "ner":
            return True
        elif Nomen[-5:] == "ismus":
            return True
        
        elif Nomen[-2:] in ["er", "or"]:
            return True
        elif Nomen[-4:] == "ling":
            return True
        elif Nomen[-3:] == "ist":
            return True
        return False

    def isFeminin(self, Nomen: str):
        
        if Nomen[-2:] in ["ie", "ik"]:
            return True
        elif Nomen[-3:] in ["tät", "ung"]:
            return True
        elif Nomen[-2:] in ["heit", "keit"]:
            return True
        elif Nomen[-6:] == "schaft":
            return True
        pass
        # -ie	z.B. die Bäckerei, die Wäscherei [A]
        # -ik	z.B. die Musik, die Physik [A]
        # -tät	z.B. die Realität, die Qualität [A]
        # -ung	z.B. die Zeitung, die Meinung [A]
        # -schaft	z.B. die Mannschaft, die Leidenschaft [A]
        # -heit	z.B. die Freiheit, die Einsamkeit [A]
        # -keit	z.B. die Möglichkeit, die Traurigkeit [A]
        
        

        # Motorradmarken 	z.B. die Suzuki, die Harley Davidson
        # Schiffsnamen 	z.B. die Queen Elisabeth, die Europa
        # Flugzeuge 		z.B. die Concorde, die Boeing
        # Zahlen 		z.B. die Eins, die Neun
        # Blumen 		z.B. die Tulpe, die Rose
        # -e	z.B. die Ente, die Lampe [U]
        # -t	z.B. die Fahrt, die Nacht [U]
        # -in	z.B. die Professorin, die Studentin [U]
        # -ur	z.B. die Manufaktur, die Agentur [U]
        # -ion	z.B. die Aktion, die Diskussion [U]
        # -age	z.B. die Passage, die Garage [U]
        # -anz	z.B. die Akzeptanz, die Toleranz [U]
        # -ade	z.B. die Limonade, die Marmelade [U]
        # -enz	z.B. die Präsenz, die Prominenz [U]


    def isNeutrum(self, Nomen: str):
        # Farben 			z.B. das Grün, das Gelb
        # Metalle 			z.B. das Silber, das Gold
        # Chemische Elementen 	z.B. das Helium, das Uran
        # Substantivierte Verben 	z.B. das Schlafen, das Lesen
        # Substantivierte Adjektive 	z.B. das Schöne, das Gute


        # -chen [A]
        # -lein [A]
        # Ge- [A]

        # -ial [U]
        # -nis [U]
        # -um [U]
        # -ment [U]
        pass

    def itCouldBe (self):
        pass