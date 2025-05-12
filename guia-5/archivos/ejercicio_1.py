## Escribir una función llamada contar (o count) que dado un archivo retorne la cantidad de filas que tiene.

import os

ruta_completa = os.path.abspath(__file__)

directorio = os.path.dirname(ruta_completa)

def contar_lineas():
    archivo = open(directorio + "/texts/e_1.txt")
    lineas = archivo.readlines()
    archivo.close()
    
    return len(lineas)

# print(contar_lineas())