def ingresar_numeros():
    numeros = []
    while (len(numeros) < 5):
        try:
            numero = int(input("Ingrese un número: "))
            numeros.append(numero)
        except ValueError:
            print("Error, debe ingresar un número entero.")
    
    return sum(numeros)

print(ingresar_numeros())