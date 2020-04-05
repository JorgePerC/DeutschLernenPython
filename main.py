#Started this program with the help of: https://www.youtube.com/watch?v=vISRn5qFrkM
#Full documentation at: https://gspread.readthedocs.io/en/latest/index.html


import gspread
from oauth2client.service_account import ServiceAccountCredentials

import pprint
import time

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('deutschLernen_credentials.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Wortschatz').worksheet("Nomen")

# words = sheet.get_all_records()

pp = pprint.PrettyPrinter()

# column = 10
# result = sheet.row_values(10)
# result = sheet.col_values(2)
# result = sheet.cell(10,10).value
# sheet.update_cell(10,10,"New Value")

# rowData = ["Genre", "Type", "Hola"]
# index = 1
# sheet.insert_row(rowData, index)
# sheet.delete_row(index)

# print(sheet.row_count) #Len of documents

# pp.pprint(words)
# pp.pprint(result)
def transportarALibro(libro, valor, fila):
    print("Moviendo la fila " + str(fila) + " con valor "+ valor +" al libro: " +  libro)
    newSheet = client.open('Wortschatz').worksheet(libro)
    rowToMove = sheet.row_values(fila)
    print("\tMoving: " + str(rowToMove))
    newSheet.insert_row(rowToMove, 1)
    #le quito una columna
    #sheet.delete_row(fila)
    del newSheet
    time.sleep(0.1)
def primerIntento():
    fila = 71 # initialization
    while fila < sheet.row_count:
        if (sheet.cell(fila, 4).value == "V." ):
            transportarALibro("Verbs","V.", fila)
            fila = fila-1
        elif (sheet.cell(fila, 4).value == "K." ):
            transportarALibro("Konnektor","K.", fila)
            fila = fila-1
        elif (sheet.cell(fila, 4).value == "P." ):
            transportarALibro("Praposition","P.", fila)
            fila = fila-1
        elif (sheet.cell(fila, 4).value == "Adj." ):
            transportarALibro("Adjektiv","Adj.", fila)
            fila = fila-1
        elif (sheet.cell(fila, 4).value == "Adv." ):
            transportarALibro("Adverb","Adv.", fila)
            fila = fila-1
        elif (sheet.cell(fila, 4).value == "Na." ):
            transportarALibro("Name","Na.", fila)
            fila = fila-1
        else:
            print(fila)
            fila = fila + 1
            time.sleep(0.2)

def segundoIntento():
    
    todosEnum = []
    ColumnaD = sheet.col_values(4)
    # Los enumerate se comportan como arrays
    for apuntador in enumerate (ColumnaD):
        todosEnum.append(apuntador)
    print(todosEnum)
    print("------------")
    for x in todosEnum:
        if not("N." in x):
            distintos_N.append(x)
    pp.pprint(distintos_N)

    # print(distintos_N[1]) #Dato
    # print(distintos_N[1][0]) #Row
#----Main----
distintos_N = []
segundoIntento()
# #Las celtas empiezan en (1,1)
# print (sheet.cell(1,1).value)

for x in distintos_N:
    if (x[1] == "V."):
        transportarALibro("Verbs","V.", x[0]+1)
    elif (x[1] == "K."):
        transportarALibro("Konnektor","K.", x[0]+1)
    elif (x[1] == "P."):
        transportarALibro("Praposition","P.", x[0]+1)
    elif (x[1] == "Adj."):
        transportarALibro("Adjektiv","Adj.", x[0]+1)
    elif (x[1] == "Adv."):
        transportarALibro("Adverb","Adv.", x[0]+1)
    elif (x[1] == "Na."):
        transportarALibro("Name","Na.", x[0]+1)
    else:
        time.sleep(.2)
        pass

#Aún falta eliminarlas de la principal:
#Las eliminamos de la cola en adelante
#Para no modificar las posiciones
#Llegamos hasta -1 para tener la posicion 0
#Del array distintos_N
for x in range (distintos_N, -1,-1):
    sheet.delete_row(distintos_N[x][0]+1)