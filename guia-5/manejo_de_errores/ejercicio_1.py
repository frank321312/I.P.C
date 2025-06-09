def obtener_contenido_archivo(nombre_archivo):
    try:
        archivo = open(f"guia-5/archivos/texts/{nombre_archivo}", "r", encoding="utf-8")
        contenido = archivo.read()
        archivo.close()
        return contenido
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

print(obtener_contenido_archivo("salas.txt"))