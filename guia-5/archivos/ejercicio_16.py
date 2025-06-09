from ejercicio_1 import directorio

def imprimir_5_lineas(archivos):
    for nombre in archivos:
        ruta = f"{directorio}/texts/{nombre}"
        try:
            abrir_archivo = open(ruta)
            lineas = abrir_archivo.readlines()
            abrir_archivo.close()
            for linea in lineas[0:5]:
                print(linea, end="")
        
        except FileNotFoundError:
            print("El archivo no existe")
            nuevo_archivo = open(ruta, mode="w")
            nuevo_archivo.close()
            print(f"Se ha creado el archivo {nombre}")
        print("---------------------------------------------------------------------------")

archivos = ["db_1.csv", "db_2.csv", "db_8.csv", "db_4.csv"]
imprimir_5_lineas(archivos)