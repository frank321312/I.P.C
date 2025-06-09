from ejercicio_1 import directorio
from ejercicio_5 import crear_archivo 

def dividir_archivo_menor_o_igual_a_10_lineas(nombre_archivo, tipo):
    archivo = open(directorio + f"/texts/{nombre_archivo}.{tipo}")
    lineas_archivo = archivo.readlines()
    archivo.close()
    
    while ("\n" in lineas_archivo):
        lineas_archivo.remove("\n")
    
    encabezado = lineas_archivo.pop(0)
    lineas = []
    
    for i in range(0, len(lineas_archivo), 9):
        bloque = lineas_archivo[i:i+9]
        eliminar_fila_vacia = bloque.pop()
        lineas.append([encabezado] + bloque + [eliminar_fila_vacia.strip()])
        
    for i in range(len(lineas)):
        crear_archivo(f"db_{i + 1}", tipo, lineas[i])
        print(f"Archivo {i + 1} creadoe existosamente.")

dividir_archivo_menor_o_igual_a_10_lineas("db", "csv")