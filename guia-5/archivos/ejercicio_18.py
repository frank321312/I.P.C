def extraer_informacion(nombre_archivo, seccion: str, inicio, final):
    archivo = open(f"guia-5/archivos/texts/{nombre_archivo}", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()
    
    informacion = [f"# {seccion}\n"] + lineas[inicio - 1:final]
    
    lower_seccion = seccion.lower()
    
    archivo_materia = open(f"guia-5/archivos/texts/{lower_seccion}.csv", mode="w", encoding="utf-8")
    archivo_materia.writelines(informacion)
    archivo_materia.close()
    
    print(f"Seccion separada en el archivo {lower_seccion}.csv")

extraer_informacion("apuntes.txt", "Matematica", 2, 4)