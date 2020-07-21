#Programa para eliminar palabras duplicadas en una hoja
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread.exceptions import APIError
import numpy as np
import pprint
#Check if there are duplicades in the book
#Read complete book
#Make list of duplicates
#Delete all but one 

class DuplicateKiller:
        
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('Credentials/deleter_credentials.json', scope)
        self.client = gspread.authorize(creds)

    def enumerateBasicValues(self, lista: list):
        enumBasicValues = []
        for i in enumerate (lista):
            enumBasicValues.append(i)
        return enumBasicValues

    def deleteDuplicatesInSheet(self, libro):
        sheet = self.client.open('Wortschatz').worksheet(libro)
        #Obtener TODOS los valores
        basicValues = sheet.get_all_records()
        repeatedValues = [] 
        enumBasicValues = self.enumerateBasicValues(basicValues) #Same length as basicValues
        # enumBasicValues[n][0] = rowNumber
        # enumBasicValues[n][1] = rowData
        print("-------")
        
        # Count duplicates
        for i in basicValues:
            repeticiones = basicValues.count(i)
            print(i)
            print("\t repeticiones: " + str(repeticiones))
            if repeticiones>1:
                repeatedValues.append([i, repeticiones])
        # repeatedValues [n][0] = dictionary with data
        # repeatedValues [n][1] = repetitions
        # repeatedValues [n][0].get("key") = desired data
        pp = pprint.PrettyPrinter()

        pp.pprint(repeatedValues)
        
        #Reverse without reversing
        for x in range (len(repeatedValues)-1, -1, -1):
            if (repeatedValues.count(repeatedValues[x])>1):
                repeatedValues.pop(x)
        print("-------")
        pp.pprint(repeatedValues)
        # repeatedValues [n][0] = word
        # repeatedValues [n][1] = repetitions
        
        if len(repeatedValues)== 0:
            print("No hay duplicados")
            return

        enumBasicValues.reverse()
        for row in enumBasicValues:
            print(row[1]) # Print dicctionary
            for RValues in repeatedValues:
                if row[1] in RValues and RValues[1]>1: #row[1] = rowData  values[1] = repeticiones
                    print("Duplicado en :" + str(RValues))
                    sheet.delete_row(row[0]+2) # Le sumo 2, porque empieza en 0, y la primera es título
                    print ("Deleted row " + str(row[0]+2) )
                    RValues[1] -= 1 # Le resta a las repeticiones
                    print("\tQuedan " + str(RValues[1]) + " repeticiones")
                    time.sleep(0.2)
                    break # Se repite, intentaré evitarlo
    
    def allWorksheetsInDoc(self):
        return self.client.open('Wortschatz').worksheets()
    

# List of all worksheets

eliminador = DuplicateKiller()
eliminador.deleteDuplicatesInSheet("Name")

#worksheets = eliminador.allWorksheetsInDoc()

# Make it work later

# for sheet in worksheets:
#     try:
#         eliminador.deleteDuplicatesInSheet(sheet)
#     except gspread.exceptions.APIError as error:
#         print("PAGE NOT FOUND ")
#         print(error)
    


#HACER UNA FUNCION QUE TE PASE TODO A LOWER O UPPER