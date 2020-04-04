import gspread
from oauth2client.service_account import ServiceAccountCredentials

import pprint

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('deutschLernen_credentials.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Wortschatz').sheet1

words = sheet.get_all_records()

pp = pprint.PrettyPrinter()

# column = 10
# result = sheet.row_values(10)
# result = sheet.col_values(10)
# result = sheet.cell(10,10).value
# sheet.update_cell(10,10,"New Value")

# rowData = ["Genre", "Type", "Hola"]
# index = 1
# sheet.insert_row(rowData, index)
# sheet.delete_row(index)

# print(sheet.row_count) #Len of documents

pp.pprint(words)