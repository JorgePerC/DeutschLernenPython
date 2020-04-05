#Programa para eliminar palabras duplicadas en una hoja
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread.exceptions import APIError

#Check if there are duplicades in the book
#Read complete book
#Make list of duplicates
#Delete all but one 

class duplicateKiller:
        
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('Credentials/deleterCredentials.json', scope)
        self.client = gspread.authorize(creds)

    def deleteDuplicatesInSheet(self, libro):
        sheet = client.open('Wortschatz').worksheet(libro)
        #Obtener 
        basicValues = sheet.col_values(1)
        repeatedValues = []
        enumBasicValues = []

        for i in enumerate (basicValues):
            enumBasicValues.append(i)

        for i in enumBasicValues:
            #Este count no va a funcionar :(
            repeticiones = basicValues.count(i)
            if repeticiones>1:
                repeatedValues.append(i)
        
        

    