#Programa para practicar verbos en participio
import random

def definirlista():
     Verbs = [
          { "verb": "gehen", "s||h": "sein", "verbImPerfekt": "gegangen"},
          { "verb": "fahren", "s||h": "sein", "verbImPerfekt": "gefahren"},
          { "verb": "reisen", "s||h": "sein", "verbImPerfekt": "gereist"},
          { "verb": "passieren", "s||h": "sein", "verbImPerfekt": "passiert"}
     ]

#Cómo obtener los valores aleatorios:
def ejemplo1():
     #lista.shuffle() no funciona. Se hace así --> 
     random.shuffle(lista)
     print(lista[0].get("verb"))

def ejemplo2():
     #El randint tiene dos valores inclusivos, por lo que le tenemos que restar uno a
     #el valor de len(lista)
     randomNumber = random.randint(0, len(lista)-1)

     print(lista[randomNumber].get("verb"))
     #Con este suelen repetirse las palabras

def ejemplo3():
     random.shuffle(lista)

     print(lista.pop().get("verb"))

def ejemplo4():
     random.shuffle(lista2)
     return lista2.pop()

     #Posiciones
     # 0 --> Verbo
     # 1 --> haben oder sein
     # 2 --> participe

#Verificar respuestas


#------------------------------ Main

#Globales
# # dic = {"Key": 5 , "Key": 5}   
# verb1 = { "verb": "gehen", "s||h": "sein", "verbImPerfekt": "gegangen"}
# verb2 = { "verb": "fahren", "s||h": "sein", "verbImPerfekt": "gefahren"}
# verb3 = { "verb": "reisen", "s||h": "sein", "verbImPerfekt": "gereist"}
# verb4 = { "verb": "passieren", "s||h": "sein", "verbImPerfekt": "passiert"}

# lista = [verb1, verb2, verb3, verb4]

lista2 = [
          ["gehen","sein","gegangen"],
          ["fahren","sein","gefahren"],
          ["reisen","sein","gereist"],
          ["passieren","sein","passiert"]
     ]

listaErrores = []

random.shuffle(lista2)

#While
while (True):

     elegido = lista2.pop()

     verbo = elegido[0]
     sein_haben= elegido[1]
     verboPartizip = elegido[2]

     print("El verbo seleccionado es: " + verbo)
     respuesta1 = input("Sein oder Haben: ")
     if respuesta1 == sein_haben:
          respuesta2 = input("Was ist sein Partizip? ")
          if respuesta2 == verboPartizip:
               print("Korrekt")
          else:
               print("Das Partizip ist inkorrekt")
               listaErrores.append(respuesta2 + " Partizip")
     else:     
          print("Falsch")
          listaErrores.append(verbo + " sein/haben")
          lista2.insert(0,elegido)
          #lista2.append(elegido)

     if(input("Seguir? ") == "no" or (len(lista2)== 0)):
          break
     else:
          pass #No hace nada, continúa

print("Te equivocaste en :")
print(listaErrores)