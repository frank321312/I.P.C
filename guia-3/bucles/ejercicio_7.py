import random

## Hacer una función que reciba un número del 1 al 10, y luego permita al usuario poder adivinar ese número, ingresando valores repetidamente. Para cada ingreso del usuario, el programa debe indicarle si su número es menor o mayor al número a adivinar. Una vez que el usuario ingresa el número correcto, lo felicita y termina.

def adivinar_numero_a():
    numero = int(input("Introduce un número entre 1 y 10: "))
    adivinar = 5
    while (numero != adivinar):
        if (numero < adivinar):
            print("El número es mayor")
        else:
            print("El número es menor")

        numero = int(input("Introduce otro número entre 1 y 10: "))

    print("¡Has adivinado el número!")

## Repetir permitiendo únicamente 3 intentos.

def adivinar_numero_b():
    count = 0
    adivinar = 5

    while True:
        numero = int(input("Introduce un número entre 1 y 10: "))
        if (numero < adivinar):
            print("El número es mayor")
        else:
            print("El número es menor")

        count += 1

        if (numero == adivinar):
            print("¡Has adivinado el número!")
            break

        if (count == 3 and numero != adivinar):
            print("Has agotado tus intentos. El número era:", adivinar)
            break

## Repetir generando el número aleatoriamente de la siguiente forma dentro de la función, sin recibirlo por parámetro:

def adivinar_numero_c():
    count = 0
    adivinar = random.randint(1, 10)
    print(adivinar)

    while True:
        numero = int(input("Introduce un número entre 1 y 10: "))

        if (numero == adivinar):
            print("¡Has adivinado el número!")
            break

        if (numero < adivinar):
            print("El número es mayor")
        else:
            print("El número es menor")

        count += 1

        if (count == 3 and numero != adivinar):
            print("Has agotado tus intentos. El número era:", adivinar)
            break