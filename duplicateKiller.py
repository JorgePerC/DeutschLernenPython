#Programa para eliminar palabras duplicadas en una hoja
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread.exceptions import APIError
import numpy as np

#Check if there are duplicades in the book
#Read complete book
#Make list of duplicates
#Delete all but one 

class DuplicateKiller:
        
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('Credentials/deleterCredentials.json', scope)
        self.client = gspread.authorize(creds)

    def enumerateBasicValues(self, lista: list):
        enumBasicValues = []
        for i in enumerate (lista):
            enumBasicValues.append(i)
        return enumBasicValues

    def deleteDuplicatesInSheet(self, libro):
        sheet = self.client.open('Wortschatz').worksheet(libro)
        #Obtener 
        basicValues = sheet.col_values(2)
        repeatedValues = [] 
        enumBasicValues = self.enumerateBasicValues(basicValues) #Same length as basicValues
        # enumBasicValues[n][0] = row
        # enumBasicValues[n][1] = word
        print("-------")
        
        # Count duplicates
        for i in enumBasicValues:
            repeticiones = basicValues.count(i[1])
            print(i)
            print("\t repeticiones: " + str(repeticiones))
            if repeticiones>1:
                repeatedValues.append([i[1], repeticiones])
        # repeatedValues [n][0] = list with (row, word)
        # repeatedValues [n][1] = repetitions
        # repeatedValues [n][0][0] = row 
        # repeatedValues [n][0][1] = word 

        print(repeatedValues)
        
        #Reverse without reversing
        for x in range (len(repeatedValues), -1, -1):
            if (repeatedValues.count(repeatedValues[x-1])>1):
                repeatedValues.pop()

        print(repeatedValues)
        # repeatedValues [n][0] = word
        # repeatedValues [n][1] = repetitions
        enumBasicValues.reverse()
        for row in enumBasicValues:
            print(row[1])
            for RValues in repeatedValues:
                if row[1] in RValues and RValues[1]>1: #row[1] = palabra  values[1] = repeticiones
                    print("Se encontró")
                    sheet.delete_row(row[0]+1)
                    print ("deleted row " + str(row[0]+1) )
                    RValues[1] -= 1 # Le resta a las repeticiones
                    time.sleep(0.2)

eliminador = DuplicateKiller()
eliminador.deleteDuplicatesInSheet("Name")


#HACER UNA FUNCION QUE TE PASE TODO A LOWER O UPPER