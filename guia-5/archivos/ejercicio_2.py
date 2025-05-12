## Escribir una funcion llamada imprimir(o cat) que dado un archivo imprima por pantalla todo el contenido.
## Agregar un parametro a la funcion llamado ignorar_vacias (o blank) que en caso de ser True, no se impriman las lineas en blanco.

from ejercicio_1 import directorio

def imprimir(ignorar_vacias = False):
    archivo = open(directorio + "/texts/e_1.txt")
    lineas = archivo.readlines()
    archivo.close()

    for i in lineas:
        print(i, end="") if ignorar_vacias else print(i) 
        
# imprimir()