from ejercicio_1 import directorio

def wc(nombre_archivo, tipo):
    archivo = open(directorio + f"/texts/{nombre_archivo}.{tipo}")
    lineas = archivo.readlines()
    archivo.close()
    contenido = sum([i.split(" ") for i in lineas], [])
    print({ "cantidad_linea": len(lineas), "cantidad_palabra": len(contenido), "cantidad_caracter": len("".join(contenido)) })

wc("e_1", "txt")