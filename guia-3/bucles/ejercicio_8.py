## Queremos modelar una máquina de sacar juguetes. Debemos hacer una función que reciba un número que representa la cantidad de fichas X que necesita la máquina para funcionar. Se debe imprimir un mensaje en pantalla que indique “Ingresá X fichas para comenzar”. El usuario deberá ingresar entonces letras “F”, que representan a las fichas. Notar que si se ingresa algo distinto a “F”, se ignora.

def maquina_sacar_juegtes(fichas_requeridas):
    ficha = input(f"Ingrese {fichas_requeridas} fichas para comenzar: ")

    while (ficha != "F" or fichas_requeridas > 1):
        fichas_requeridas -= 1 and ficha == "F"
        ficha = input(f"Ingrese {fichas_requeridas} fichas para comenzar: ")
    
    print("¡A jugar!")

maquina_sacar_juegtes(3)