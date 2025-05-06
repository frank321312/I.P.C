## Imprima por pantalla todos los números entre 10 y 20.

def imprimir_numeros_entre_10_y_20():
    for i in range(10, 21):
        print(i)

## salude a cada una de las siguientes personas: Flaminia, Serena, Agustina, Priscila, Sol, Agostina, Iara y Lu.
## Para cada saludo, use la frase: "Hola <nombre>! Vamos a aprender a programar".

def imprimir_saludo():
    for i in ["Flaminia", "Serena", "Agustina", "Priscila", "Sol", "Agostina", "Iara", "Lu"]:
        print("Hola <nombre>! Vamos a aprender a programar".replace("<nombre>", i))

## Le pida al usuario que ingrese 5 números y le muestre la suma total de todos ellos.

def suma_total():
    suma = 0
    for i in range(5):
        numero = int(input("Ingrese un numero: "))
        suma += numero
    print(suma)

## Imprima por pantalla todos los números entre 100 y 199 que sean divisibles por 7.

def divisible_por_7():
    for i in range(100, 200):
        if i % 7 == 0:
            print(i)

## Reciba dos números, y recorra todos los números entre ellos, imprimiendo en pantalla si es par o impar.

def es_par_o_impar(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(f"{i} es par")
        else:
            print(f"{i} es impar")