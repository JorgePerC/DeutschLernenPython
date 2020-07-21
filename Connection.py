
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread.exceptions import APIError
import pandas as pd

#This code will function as a conection to the database

"""
There will be three types of connection usecase:
    deleter
    deutschLernen
    requests_SJ
By default, request "requests_SJ" will stablish the conection
"""
class SheetConnection:
    def __init__(self, sheetName: str,  usecase = "requests_SJ"):
        credentialsFile = "Credentials/" + usecase + "_credentials.json"
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentialsFile, scope)
        self.client = gspread.authorize(creds)
        self.sheet = self.client.open('Wortschatz').worksheet(sheetName)
        print("You are currently conected to the {} sheet".format(sheetName))

    # Method to get all the data from the sheet 
    # Returns it as a pd dataframe   
    # VERIFIED
    def getDataWithPandas(self):
        dataFrame = pd.DataFrame (self.sheet.get_all_records())
        return dataFrame
    
    # Method to get all the data from the sheet 
    # Returns it as a list of lists
    # VERIFIED
    def getData(self):
        return self.sheet.get_all_records()
    # Method to update the data
    # Method to know all the characteristics to fill
    # Method to close connection?
    # Verify if "casilla de verificación" returns a boolean
