## Piedra, papel o tijera: escribir un programa de “Piedra, papel o tijera” tal que sea imposible que el usuario gane. El usuario debe ingresar R (piedra), P (papel), o T (tijera) y la computadora debe siempre ganarle

def cuarzo_papiro_o_navaja():
    print("¡Cuarzo (C), papiro (P) o navaja (N)!")
    jugada = input("Ingrese jugada: ")
    jugada_lower = str.lower(jugada)

    if (jugada_lower == "c"):
        print("¡Papito! ¡Gané!")
    elif (jugada_lower == "p"):
        print("¡Navaja! ¡Gané!")
    elif (jugada_lower == "n"):
        print("¡Cuarzo! ¡Gané!")
    else:
        print("Jugada no valida")

cuarzo_papiro_o_navaja()