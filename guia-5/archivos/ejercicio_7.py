## Escribir una función, llamada grep, que reciba una cadena y un archivo de texto, e imprima las líneas del archivo que contienen la cadena recibida.

from ejercicio_1 import directorio

def grep(cadena, nombre_archivo, tipo):
    archivo = open(directorio + f"/texts/{nombre_archivo}.{tipo}")
    lineas = archivo.readlines()
    archivo.close()
    for linea in lineas:
        if cadena in linea:
            print(linea.strip())

grep("mensaje", "e_1", "txt")