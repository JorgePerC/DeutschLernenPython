"""
In this file, you will be able to test all the methods
from the implemented clasess, feel free to modify it 
as much as you want, there is no problem :)
"""

from Connection import SheetConnection
from Worte import Worte

# conectionTest = SheetConnection("Verbs")
# print(conectionTest.getAttributes())

palabra = Worte ()
print(palabra.selectedRow)
print(palabra.getUbersetzung())
