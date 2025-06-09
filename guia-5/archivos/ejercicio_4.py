## Escribir una función llamada ver_final (o tail) que dado un archivo y un número N retorne en una lista las últimas N lineas del archivo.

from ejercicio_1 import directorio

def ver_final(n: int, nombre_archivo, tipo):
    archivo = open(directorio + f"/texts/{nombre_archivo}.{tipo}")
    lineas = archivo.readlines()
    archivo.close()

    return lineas[-n:]

print(ver_final(2, "e_1", "txt"))