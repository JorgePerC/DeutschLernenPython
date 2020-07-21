
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread.exceptions import APIError

#This code will function as a conection to the database

"""
There will be three types of connection usecase:
    deleter
    deutschLernen
    requests_SJ
By default, request "requests_SJ" will stablish the conection
"""
class Connection:
    def __init__(self, usecase = "requests_SJ"):
        credentialsFile = "Credentials/" + usecase + "_credentials.json"
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentialsFile, scope)
        self.client = gspread.authorize(creds) 
    
    #Page name, aka, sheet book, aka, libro
    def openBook(self, sheetName):
        sheet = self.client.open('Wortschatz').worksheet(sheetName)

    # Method to get all the data from the sheet
    # Method to update the data
    # Method to know all the characteristics to fill
    # Method to close connection?
    # Verify if "casilla de verificación" returns a boolean
