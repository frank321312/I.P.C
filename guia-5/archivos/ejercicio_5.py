## Escribir una función llamada crear (o touch) que dado el nombre de un archivo lo cree. Si el archivo exixte borra todo el contenido.

from ejercicio_1 import directorio

def crear(nombre: str):
    archivo = open(directorio + f"/texts/{nombre}.txt", "w")
    archivo.close()

crear("test")