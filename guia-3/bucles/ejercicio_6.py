## Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.

def ingresar_contrasena_a():
    contrasena = input("Ingrese la contraseña: ")
    password = "Contraseña"

    while (contrasena != password):
        print("Contraseña incorrecta")
        contrasena = input("Ingrese la contraseña: ")
    
    print("Contraseña correcta")

## Modificar el programa anterior para que solamente permita una cantidad fija de intentos.

def ingresar_contrasena_b():
    count = 0
    contrasena = input("Ingrese la contraseña: ")
    password = "Contraseña"

    while (contrasena != password and count < 5):
        print("Contraseña incorrecta")
        contrasena = input("Ingrese la contraseña: ")
        count += 1

    if (contrasena == password):
        print("Contraseña correcta")


## Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).

def ingresar_contrasena_c():
    contrasena = input("Ingrese la contraseña: ")
    password = "Contraseña"    

    if (contrasena == password):
        return True
    else:
        return False