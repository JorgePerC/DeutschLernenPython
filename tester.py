"""
In this file, you will be able to test all the methods
from the implemented clasess, feel free to modify it 
as much as you want, there is no problem :)
"""

from Connection import SheetConnection
from Worte import Worte
from Nomen import Nomen
from Verb import Verb
import pandas as pd

# conectionTest = SheetConnection("Verbs")
# df = conectionTest.getDataWithPandas()

# print(df.keys().values)
# print(df.sample().values)

palabra = Worte ()
print(palabra.attributes)
print(palabra.get_Ubersetzung())

# sustantivo = Nomen()
# print("palabra: {}".format(sustantivo.wort))
# print("palabra: {}".format(sustantivo.artikel))
print("---------------")
verbo = Verb()
print(verbo.attributes)
print(verbo.conjugate_in_present("ich"))

print("Hello World")