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

sheet = client.open('Wortschatz').worksheet("Adjektiv2")
words = sheet.get_all_records()
listaErrores = []
listaErrores2 = []


def conjugarKyS(adjetivoElegido):
    listaKyS = []  
    komparativ = adjetivoElegido + ("er")
    listaKyS.append(komparativ)
    if adjetivoElegido[-1] == "t":
        adjetivoElegido = adjetivoElegido + ("esten")
    else:
        adjetivoElegido = adjetivoElegido + ("sten")
    listaKyS.append(adjetivoElegido)
    return listaKyS

def iniciarApp():
    random.shuffle(words)
    while not (len(words)== 0):
        palabra = words.pop(-1)
        adjetivoElegido = palabra.get("Wort")
        palabraEspañol = palabra.get("Übersetzung")
        konjugados = conjugarKyS(adjetivoElegido)
        print(adjetivoElegido)
        respuesta = input("Schreibe sie der Übersetzung ")
        if respuesta in palabraEspañol:
            print("Korrekt")
            respuesta1 = input("Schreibe sie der komparativ ")
            if respuesta1 in konjugados:
                print("Korrekt")
                respuesta2 = input("Schreibe sie die Superlativ ")
                if respuesta2 in konjugados:
                    print("Korrekt")
                else:
                    print("Inkorrekt")
                    listaErrores.append(respuesta2 + "superlativ incorrecto, el correcto es " + konjugados[1])
                    listaErrores2.append(adjetivoElegido)
            else:
                print("Inkorrekt")
                listaErrores.append(respuesta1 + "komparativ incorrecto, el correcto es " + konjugados[0])
                listaErrores2.append(adjetivoElegido)
        else:
            print("Inkorrekt")
            listaErrores.append(respuesta + "Übersetzung incorrecto, el correcto es " + palabraEspañol)
            listaErrores2.append(adjetivoElegido)
        frage = input("Wollst du weiterführen ")
        if frage == "no":
            break


iniciarApp(words)
respuestaTry = input("Willst du noch einaml die Fehler wiederholen ")
if respuestaTry == "si":
    iniciarApp(listaErrores2)
else:
    print(listaErrores)
                

            

                



#MAIN
