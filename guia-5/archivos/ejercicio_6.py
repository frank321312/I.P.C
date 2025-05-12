from ejercicio_1 import directorio

def wc():
    archivo = open(directorio + "/texts/e_1.txt")
    lineas = archivo.readlines()
    archivo.close()
    contenido = sum([i.split(" ") for i in lineas], [])

    print({ "cantidad_linea": len(lineas), "cantidad_palabra": len(contenido), "cantidad_caracter": len("".join(contenido)) })
    
wc()