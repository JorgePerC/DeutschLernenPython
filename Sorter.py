# Programa para clasificar las palabras desde el libro donde se guardan todas
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
from gspread.exceptions import APIError
from oauth2client.transport import request

class Sorter:
    def __init__(self): 

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('Credentials/deutschLernen_credentials.json', scope)
        self.client = gspread.authorize(creds)

        self.sheet = client.open('Wortschatz').worksheet("Gemischt")
        self.distintos_N = []
    
    def enumVerbs(self):
        columna_D_Enum = []
        ColumnaD = self.sheet.col_values(1)
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
                self.distintos_N.append(x)
        # La imprimo para corroborar el resultado
        
    def clasificar(self, libro, valor, fila):
        # Porque cuando meto mi sleep al inicio funciona
        time.sleep(0.2) 
        print("Moviendo la fila " + str(fila) + " con valor "+ valor +" al libro: " +  libro)
        # New sheet es el libro a dónde voy a mandar los datos
        newSheet = self.client.open('Wortschatz').worksheet(libro)
        rowToMove = self.sheet.row_values(fila)
        print("\tMoving: " + str(rowToMove))
        # Insertamos rowToMove al inicio 
        newSheet.insert_row(rowToMove, 2)
        # Elimino el libro abierto, para evitar requests que no pedí
        del newSheet
        # Una vez que ya lo cambié de libro, meto la fila al array
        # de rowsToDelete para que después sea eliminada de la primera hoja
        sheet.delete_row(fila)
    
    def ejecutarOrden(self):
        enumVerbs()
        try:
            # Le aplique el reverse, se supone que 
            self.distintos_N.reverse()
            for x in self.distintos_N:
                if (x[1] == "V."):
                    clasificar("Verbs","V.", x[0]+1)
                elif (x[1] == "K."):
                    clasificar("Konnektor","K.", x[0]+1)
                elif (x[1] == "P."):
                    clasificar("Praposition","P.", x[0]+1)
                elif (x[1] == "Adj."):
                    clasificar("Adjektiv","Adj.", x[0]+1)
                elif (x[1] == "Adv."):
                    clasificar("Adverb","Adv.", x[0]+1)
                elif (x[1] == "Na."):
                    clasificar("Name","Na.", x[0]+1)
                else:
                    time.sleep(.2)
                    pass
            print("Se clasificaron todos")
        except gspread.exceptions.APIError as error:
            print("NO se TERMINÓ de Revisar, causado por: ")
            print(error)

# TRYME
ordenador = Sorter()
ordenador.ejecutarOrden()