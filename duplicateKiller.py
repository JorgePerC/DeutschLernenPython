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
    def countDuplicates (self, lista: list):
        pass

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
            # print(i)
            # print("\t repeticiones: " + str(repeticiones))
            if repeticiones>1:
                repeatedValues.append([i[1], repeticiones])
        # repeatedValues [n][0] = list with (row, word)
        # repeatedValues [n][1] = repetitions
        # repeatedValues [n][0][0] = row 
        # repeatedValues [n][0][1] = word 

        print(repeatedValues)

        

        print(repeatedValues)

            # repeatedValues [n][0] = word
            # repeatedValues [n][1] = repetitions
                

eliminador = DuplicateKiller()
eliminador.deleteDuplicatesInSheet("Praposition")