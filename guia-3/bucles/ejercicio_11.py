## Crear una función que reciba dos números, y devuelva la suma de todos los números múltiplos de 7 entre esos dos números.

def calcular_multiplo_7_suma(start, end):
    suma = 0
    for i in range(start, end + 1):
        if (i % 7 == 0):
            suma += i

    return suma

## Repetir calculando el promedio en vez de la suma.

def calcular_multiplo_7_promedio(start, end):
    suma = 0
    contador = 0
    for i in range(start, end + 1):
        if (i % 7 == 0):
            suma += i
            contador += 1

    return suma / contador if contador > 0 else 0

## Repetir calculando únicamente el promedio entre los primeros 3 múltiplos de 7 encontrados.

def calcular_multiplo_7_promedio_3_primeros_multuplos(start, end):
    suma = 0
    contador = 0
    for i in range(start, end + 1):
        if (i % 7 == 0):
            suma += i
            contador += 1
        if (contador == 3):
            break

    return suma / contador if contador > 0 else 0

## Repetir calculando únicamente el promedio entre los múltiplos de 7 encontrados que no sean múltiplos de 2.

def calcular_multiplo_7_promedio_excepto_multiplo_2(start, end):
    suma = 0
    contador = 0
    for i in range(start, end + 1):
        if (i % 7 == 0 and i % 2 != 0):
            suma += i
            contador += 1

    return suma / contador if contador > 0 else 0

print(calcular_multiplo_7_suma(3, 29))
print(calcular_multiplo_7_promedio(3, 25))
print(calcular_multiplo_7_promedio_3_primeros_multuplos(3, 15))
print(calcular_multiplo_7_promedio_excepto_multiplo_2(3, 14))