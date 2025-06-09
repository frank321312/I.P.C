from ejercicio_1 import directorio
def calcular_promedio_producto(nombre_archivo, producto: str):
    leer_archivo = open(directorio + f"/texts/{nombre_archivo}.txt")
    
    filtrar_producto = list(filter(lambda x: x.split(";")[0].lower() == producto.lower(), leer_archivo.readlines()))
    
    leer_archivo.close()
    
    precio_promedio = sum([int(i.split(";")[1]) for i in filtrar_producto]) / len(filtrar_producto)
    
    return precio_promedio

print(calcular_promedio_producto("productos", "Arroz"))