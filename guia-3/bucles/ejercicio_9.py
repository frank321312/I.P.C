## Crear una función que calcule si un número es primo o no. Un número es primo cuando solamente es divisible por sí mismo y por 1.

def es_primo(numero):
    for i in range(2, numero):
        if (numero % i == 0):
            return False
    return True

print(es_primo(25))