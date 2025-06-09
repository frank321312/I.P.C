## Escribir una función llamada crear (o touch) que dado el nombre de un archivo lo cree. 
## Si el archivo exixte borra todo el contenido.

from ejercicio_1 import directorio

def crear_archivo(nombre, tipo, contenido = []):
    archivo = open(directorio + f"/texts/{nombre}.{tipo}", "w")
    archivo.writelines(contenido)
    archivo.close()

crear_archivo("test", "txt")