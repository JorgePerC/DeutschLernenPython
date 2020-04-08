#Programa para practicar Whiles, fors, listas bidimensionales, funciones
import time
grid = [
        ["A|1", "B|1", "C|1 ", "D|1", "E|1"],
        ["A|2", "B|2", "C|2 ", "D|2", "E|2"],
        ["A|3", "B|3", "C|3 ", "D|3", "E|3"],
        ["A|4", "B|4", "C|4 ", "D|4", "E|4"]
    ]
#---While--
def while_ejemplo_1():
    # Supongamos que le damos instrucciones a un coche.
    # Cuáles serían esas instrucciones si queremos dibujar 
    # la siguiente trayectiria:
    # — — ┬ — — ┬ — —>
    #     |     |
    #     └ — — ┘
    # Supon que cada línea es una es un paso 
    pass
def while_ejemplo_2():
    while True:
        print("Hola")
        # 1
        # if input("") == "stop":
        #     break
        while True:
            print("\tAdentro")
        #while False:
            # Qué pasa si se vuelve un False?
            

#---FOR--
def for_ejemplo_1():
    
    #Muestra la fila 3
    print()

    #Muestra la celda D2
    print()

    # Cuando trabajas con fors, hay dos maneras de acceder a los datos
    # Mostrar un grid ordenado:
    # Primera manera:
    for y in range (0, len(grid)):
        for x in range (0, len(grid[y])):
            print(grid[y][x], end= " ")
            time.sleep(0.2)
        print()

def for_ejemplo_2():
    # Cuenta del 00-99
    # No se vale sumar
    pass

def for_ejemplo_3():
    # Cuando trabajas con fors, hay dos maneras de acceder a los datos
    # Mostrar un grid ordenado:
    # Segunda manera: //Esta sólo funciona en Python
    for fila in grid:
        print(fila)
        time.sleep(0.2)
    # Como te habrás dado cuenta, me regresa una fila, 
    # Por eso podemos hacer esto:
    print("-----")
    for fila in grid:
        print(fila[0])
        time.sleep(0.2)
        # Qué va a pasar cuando intentemos
        # print(fila[] []) ?
    print("-----")
    #Cómo podemos mostrar el grid anterior con esta técnica?
    for fila in grid:
        for celda in fila:
            print(celda, end = " ")
            time.sleep(0.2)
        print()

#---funcion--
def funcion_ejemplo_1(arg1, arg2):
    print(arg1 + arg2)
    for x in range (arg1, arg2):
        print(x)
    pass




for_ejemplo_3()