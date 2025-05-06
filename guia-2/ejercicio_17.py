## Escribir una función que convierta un valor dado en grado Celsius, a Fahrenheit. Recordar que la fórmula para la conversión es: F = 9/5 * C + 32.
## Escribir una función que convierta un valor dado en grados Fahrenheit, a Celsius. Usar la misma fórmula anterior.

def convirtir_celcius_a_fahrenheit(grados_celcius):
    return round(9/5 * grados_celcius + 32, 2)

def convertir_fahrenheit_a_celcius(grados_fahrenheit):
    return round((grados_fahrenheit - 32) * 5/9, 2)

print(convirtir_celcius_a_fahrenheit(100))
print(convertir_fahrenheit_a_celcius(212))