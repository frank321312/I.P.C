## Escribir una función llamada ver_final (o tail) que dado un archivo y un número N retorne en una lista las últimas N lineas del archivo.

from ejercicio_1 import directorio

def ver_encabezado(n: int):
    archivo = open(directorio + "/texts/e_1.txt")
    lineas = archivo.readlines()
    archivo.close()

    return lineas[-n:]

print(ver_encabezado(2))