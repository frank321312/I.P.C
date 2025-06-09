from ejercicio_1 import directorio

archivos = ["archivo1.txt", "archivo2.txt"]

def procesar_archivos(archivos, palabra):
    reportes = [["archivo","palabras","apariciones"]]
    
    for archivo in archivos:
        procesar_archivo = open(directorio + f"/texts/{archivo}", encoding="utf-8")
        contenido = procesar_archivo.read()
        procesar_archivo.close()
        cantidad_palabras = len(contenido.split(" "))
        cantidad_apariciones = contenido.count(palabra)
        reportes.append([archivo, str(cantidad_palabras), str(cantidad_apariciones)])
    
    archivo_reporte = open(directorio + "/texts/reporte_plagio.txt", "w")
    
    for reporte in reportes:
        archivo_reporte.write(f"{reporte[0]};{reporte[1]};{reporte[2]}\n")
        
    archivo_reporte.close()
    
procesar_archivos(archivos, "Nick")