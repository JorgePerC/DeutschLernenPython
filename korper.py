#Programa para practicar las partes del cuerpo

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import pprint
import time
from gspread.exceptions import APIError
from oauth2client.transport import request
import random

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Credentials/requests_SJ_Credentials.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Wortschatz').worksheet("Korp")
words = sheet.get_all_records()
listaErrores1 = []
listaErrores2 = []
def iniciarApp(diccionario):
    random.shuffle(diccionario)
    # Lo que pasa aquí, que se repita la misma palabra es porque
    # filaAleman = diccionario.pop(1)
    # palabraAleman = filaAleman.get("Wort")...
    # Está fuera del While, entonces, eso no se repite.
    # Lo voy a meter.

    while not(len(diccionario) == 0): #Aquí corregí un paréntesis. Antes "not(len(diccionario)) == 0:"
        filaAleman = diccionario.pop(-1)
        palabraAleman = filaAleman.get("Wort")
        palabraEspñaol = filaAleman.get("Übersetzung")
        palabraGenero = filaAleman.get("Artikel")
        palabraPlural = filaAleman.get("Pural")
        
        print(palabraAleman)
        #Me dí todo lo de arriba
        respuesta1 = input("género ")
        if respuesta1 in palabraGenero:
            respuesta2 = input("plural ")
            if respuesta2 in palabraPlural:
                respuesta3 = input("español ")
                if respuesta3 in palabraEspñaol:
                    print("Korrekt")
                else:
                    print("Inkorrect")
                    listaErrores1.append(respuesta3 + "palabra en español incorrecta, el correcto es " + palabraEspñaol)
                    listaErrores2.append(filaAleman)
            else:
                print("Inkorrect")
                listaErrores1.append(respuesta2 + " plural incorrecto, el correcto es " + palabraPlural)
                listaErrores2.append(filaAleman)
        else:
            print("Inkorrect")
            listaErrores1.append(respuesta1 + " género incorrecto el correcto es " + palabraGenero)
            listaErrores2.append(filaAleman)
        
        if (input("Seguir? ") == "no"): 
            break
        else:
            pass


#-----Main-----
iniciarApp(words)
respuestaTry = input("Willst du noch einaml die Fehler wiederholen ")
if respuestaTry == "si":
    iniciarApp(listaErrores2)
else:
    print(listaErrores1)
    
# Funcionó bien una vez, después:
# TypeError: argument of type 'NoneType' is not iterable
# Fue porque modifiqué el docs, jajaja

#Cuando revisas los errores, y sólo tienes uno, al hacerle el pop(1)
#Te manda error

# column = 10
# result = sheet.row_values(10)
# result = sheet.col_values(2)
# result = sheet.cell(10,10).value
# sheet.update_cell(10,10,"New Value")

# rowData = ["Genre", "Type", "Hola"]
# index = 1
# sheet.insert_row(rowData, index)
# sheet.delete_row(index)

# print(sheet.row_count) #Len of documents