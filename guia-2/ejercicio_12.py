## Crear una función que le pida al usuario su nombre y apellido, e los imprima con el siguiente formato: “Apellido, Nombre”.

def ingresar_nombre_apellido():
    nombre = input("Introduce tu nombre: ")
    apellido = input("Introduce tu apellido: ")
    print(f"Nombre: {nombre}, Apellido: {apellido}")

ingresar_nombre_apellido()