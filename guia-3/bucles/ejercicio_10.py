## Crear una función que reciba un número entero e imprima los números primos entre 0 y el número ingresado.

def imprimir_numero_primo(numero):
    for i in range(1, numero + 1):
        contador = 0
        for x in range(1, numero + 1):
            if (i % x == 0):
                contador += 1

        if (contador == 2):
            print(i)

imprimir_numero_primo(5)