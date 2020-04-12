# Programa para practicar verbs

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