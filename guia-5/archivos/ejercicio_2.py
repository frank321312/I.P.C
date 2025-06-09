## Escribir una funcion llamada imprimir(o cat) que dado un archivo imprima por pantalla todo el contenido.
## Agregar un parametro a la funcion llamado ignorar_vacias (o blank) que en caso de ser True, no se impriman las lineas en blanco.

from ejercicio_1 import directorio

def imprimir(nombre_archivo, tipo, ignorar_vacias=False):
    archivo = open(directorio + f"/texts/{nombre_archivo}.{tipo}")
    lineas = archivo.readlines()
    archivo.close()
    for i in lineas:
        if ignorar_vacias:
            if i.strip():
                print(i, end="")
        else:
            print(i, end="")

# imprimir("e_1", "txt")