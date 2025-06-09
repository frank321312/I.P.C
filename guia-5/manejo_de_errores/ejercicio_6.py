sala = {"A":["L","O","O","O","L","L","L"], "B": ["L","O","O","O","L"]}

def reservar_asiento(asientos, fila, ubicacion):
    try:
        if (asientos[fila][ubicacion] != "O"):
            asientos[fila][ubicacion] = "O"
            return asientos
        print("El asiento ya se encuentra ocupado")
    except KeyError:
        print("Error: La fila no existe")
    except IndexError:
        print("Error: La ubicacion no existe")

print(reservar_asiento(sala, "A", 0))