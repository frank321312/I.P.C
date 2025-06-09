from ejercicio_1 import directorio

def salir(caracter: str):
    return caracter.lower() == 'x'

def ingresar_producto(nombre_archivo, tipo):
    archivo_modificar = open(directorio + f"/texts/{nombre_archivo}.{tipo}", "a")
    
    while True:
        print("Presione 'x' para salir.")
        nombre = input("Ingrese el nombre del producto: ")
        if salir(nombre):
            break

        codigo = input("Ingrese el código de barras: ")
        if salir(codigo):
            break

        cantidad = input("Ingrese la cantidad del producto: ")
        if salir(cantidad):
            break

        precio = input("Ingrese el precio del producto: ")
        if salir(precio):
            break

        archivo_modificar.write(f"{nombre};{codigo};{cantidad};{precio}\n")
        print("------------------Producto ingresado correctamente.------------------")
        
    archivo_modificar.close()
    print("Se ha finalizado el ingreso de productos.")
    
ingresar_producto("productos", "csv")