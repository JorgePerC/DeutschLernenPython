#Started this program with the help of: https://www.youtube.com/watch?v=vISRn5qFrkM
#Full documentation at: https://gspread.readthedocs.io/en/latest/index.html

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import pprint
import time
from gspread.exceptions import APIError
from oauth2client.transport import request

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Credentials/deutschLernen_credentials.json', scope)
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
    # Porque cuando meto mi sleep al inicio funciona
    time.sleep(0.2) 
    print("Moviendo la fila " + str(fila) + " con valor "+ valor +" al libro: " +  libro)
    # New sheet es el libro a dónde voy a mandar los datos
    newSheet = client.open('Wortschatz').worksheet(libro)
    rowToMove = sheet.row_values(fila)
    print("\tMoving: " + str(rowToMove))
    # Insertamos rowToMove al inicio 
    newSheet.insert_row(rowToMove, 1)
    # Elimino el libro abierto, para evitar requests que no pedí
    del newSheet
    # Una vez que ya lo cambié de libro, meto la fila al array
    # de rowsToDelete para que después sea eliminada de la primera hoja
    rowsToDelete.append(fila)
    #print("\t\t rowsToDelete = " + str(rowsToDelete))

def enumVerbs():
    columna_D_Enum = []
    ColumnaD = sheet.col_values(4)
    # Los enumerate se comportan como arrays
    # Lo que hacen es que te cuentan las posiciones de los elementos
    # Los vamos a ocupar para conocer las filas de los valores
    # Diferentes a "N."
    for apuntador in enumerate (ColumnaD):
        #Meto TODOS los elementos de mi sheet en el array
        columna_D_Enum.append(apuntador)
    # Puedes ver el print, para entender mejor el resultado :)
    # print(columna_D_Enum)
    print("------------")

    # Ahora creo una lista sólo con los valores diferentes a "N."
    for x in columna_D_Enum:
        if not("N." in x):
            distintos_N.append(x)
    # La imprimo para corroborar el resultado
    pp.pprint(distintos_N)


#----------Main----------

#Toma en cuenta lo siguiente:
    # #Las celtas empiezan en (1,1)
    # print(distintos_N[1]) #Dato
    # print(distintos_N[1][0]) #Row

distintos_N = []
rowsToDelete = []
enumVerbs()

try:
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
except  gspread.exceptions.APIError as error:
    print("Its an incomplete check up, CAUSED BY: ")
    print(error)

finally:
    #Aún falta eliminarlas de la principal:
    #Las eliminamos de la cola en adelante
    #Para no modificar las posiciones
    #Llegamos hasta -1 para tener la posicion 0
    #Del array distintos_N
    
    for x in range (len(rowsToDelete)-1, -1,-1):
        sheet.delete_row(rowsToDelete[x])
        time.sleep(0.2)
        print("Just deleted row:" + str(rowsToDelete[x]))
        #sheet.delete_row(distintos_N[x][0]+1)
    print()
    print("But is now clean")
