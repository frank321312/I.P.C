## Escribir una función llamada ver_encabezado (o head) que dado un archivo y un número N retorne en una lista las primeras N lineas del archivo.

from ejercicio_1 import directorio

def ver_encabezado(n: int, nombre_archivo, tipo):
    archivo = open(directorio + f"/texts/{nombre_archivo}.{tipo}")
    lineas = archivo.readlines()
    archivo.close()
    return lineas[:n]

print(ver_encabezado(2, "e_1", "txt"))