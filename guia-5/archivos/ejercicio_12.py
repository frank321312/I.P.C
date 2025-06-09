from ejercicio_1 import directorio

def reemplazar_palabra(nombre_archivo, tipo, palabra_a_reemplazar, nueva_palabra):
    archivo_leer = open(directorio + f"/texts/{nombre_archivo}.{tipo}")
    contenido = archivo_leer.read()
    archivo_leer.close()
    archivo_modificar = open(directorio + f"/texts/{nombre_archivo}.{tipo}", "w")
    contenido_modificado = contenido.replace(palabra_a_reemplazar, nueva_palabra)
    archivo_modificar.write(contenido_modificado)
    archivo_modificar.close()
    print("Archivo modificado correctamente.")

reemplazar_palabra("more", "txt", "Python", "JavaScript")