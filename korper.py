#Programa para practicar las partes del cuerpo

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import pprint
import time
from gspread.exceptions import APIError
from oauth2client.transport import request

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Credentials/requests_SJ_Credentials.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Wortschatz').worksheet("Korp")
words = sheet.get_all_records()
listaErrores1 = []
listaErrores2 = []
def iniciarApp(diccionario):
    random.shuffle(diccionario)
    filaAleman = diccionario.pop(1)
    palabraAleman = filaAleman.get("Wort")
    palabraEspñaol = filaAleman.get("Übersetzung")
    palabraGenero = filaAleman.get("Artikel")
    palabraPlural = filaAleman.get("Pural")
    
    print(palabraAleman) 
    while not(len(diccionario)) == 0:
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

iniciarApp(words)
respuestaTry = input("Willst du noch einaml die Fehler wiederholen ")
if respuestaTry == "si":
    iniciarApp(listaErrores2)
else:
    print(listaErrores1)




    
   



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