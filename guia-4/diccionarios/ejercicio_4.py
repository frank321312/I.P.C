## Se tiene una agenda implementada como diccionario, que guarda nombres de personas y sus números de teléfono. Escribir un programa que le pida al usuario que ingrese nombres.
## a.Si el nombre se encuentra en la agenda, debe mostrar el teléfono.
## b.Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
## En ambos casos, El usuario puede utilizar la palabra “EXIT” para dejar de ingresar nombres.

def agendar_persona():
    diccionario_persona = {}

    nombre = input("Ingrese un nombre ('EXIT' para salir): ")

    while (nombre != "EXOT"):
        if (nombre in diccionario_persona):
            print(f"Nombre: {nombre}, telefono: {diccionario_persona[nombre]}")
        else:
            telefono = input(f"Ingrese el telefono de {nombre} ('EXIT' para salir): ")
            if (telefono == "EXIT"):
                break
            elif (not telefono.isdigit()):
                print("Debe ser un numero valido")
                continue

            diccionario_persona[nombre] = telefono

        nombre = input("Ingrese un nombre ('EXIT' para salir): ")

agendar_persona()