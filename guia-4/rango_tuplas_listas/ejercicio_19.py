## Se tiene una matriz de 10x10 que representa un tablero. Cada celda contiene un 0 si está vacía, o un 1 si hay un barco (consideramos que en este caso, sólo hay barcos unitarios que ocupan un espacio).

## La posición de los barcos se representa con tuplas de (fila, columna). Por ejemplo, si se tiene un barco en la fila 1, columna 3, se representa con la tupla (1, 3).

## Escribir una función que cree un tablero con 10 barcos ubicados aleatoriamente (usar la biblioteca random), y que permita al usuario intentar adivinar dónde están.

## El usuario luego ingresa una posición, y la máquina indica si había un barco en esa posición (mostrando un mensaje por pantalla “¡Hundido!”) o no (“¡Agua!”).

## El usuario gana cuando hunde todos los barcos del tablero. Si se equivoca más de 5 veces, pierde.

from random import shuffle

def batalla_naval():
    pre_tablero = [1 if i <= 9 else 0 for i in range(100)]
    shuffle(pre_tablero)

    contador = 0
    tablero = []
    fila = []
    jugadas = []


    for i in pre_tablero:
        fila.append(i)
        contador += 1
        if (contador == 10):
            tablero.append(tuple(fila))
            fila = []
            contador = 0

    print(tablero)
    jugada = input("Ingrese la posicion (formato: 0-1): ")
    while (len(jugadas) != 9 and contador != 4):
        posicion = tuple(jugada.replace("-", ""))
        posicion_valor = tablero[int(posicion[0])][int(posicion[1])]

        if (posicion_valor == 1 and posicion not in jugadas):
            jugadas.append(posicion)
            print("¡Hundido!")
        elif (posicion in jugadas):
            print("Solo hay un barco hundido")
            contador += 1
        else:
            print("¡Agua!")
            contador += 1

        jugada = input("Ingrese la posicion (formato: 0-1): ")

    print("Has perdido") if contador == 4 else print("Has gamado")

batalla_naval()