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


    def deleteDuplicatesInSheet(self, libro):
        sheet = self.client.open('Wortschatz').worksheet(libro)
        #Obtener 
        basicValues = sheet.col_values(2)
        repeatedValues = [] 
        enumBasicValues = [] #Same length as basicValues
        
        #Inner funtions. Only exists in Python, that I know
        def fack():
            pass
        def create_enumBasicValues():
            for i in enumerate (basicValues):
                enumBasicValues.append(i)
            print(enumBasicValues)
            print("-------")
            # enumBasicValues[n][0] = row
            # enumBasicValues[n][1] = word

        #To make sure it actually runs create_enumBasicValues()   
        create_enumBasicValues()  
        def create_repeatedValues():
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

            for value in repeatedValues:
                if value[1] in repeatedValues:
                    print(value[0][1])
            print(repeatedValues)

            # repeatedValues [n][0] = word
            # repeatedValues [n][1] = repetitions
                

eliminador = DuplicateKiller()
eliminador.deleteDuplicatesInSheet("Praposition")