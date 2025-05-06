## Guardar los números 1, 2 y 3 en tres variables distintas y luego sumarlos e imprimir el resultado por pantalla.
## Repetir con las distintas operaciones disponibles que se vieron en la unidad 2: 
## resta, multiplicación, división, división entera, resto, potencia; combinando los números entre sí.

num_uno = 1
num_dos = 2
num_tres = 3

## Suma
resultado_suma = num_uno + num_dos + num_tres
print("Suma:")
print(resultado_suma)

## Resta
resulta_resta = num_uno - num_dos - num_tres
print("Resta:")
print(resulta_resta)

## Multiplicacion
resultado_multiplicacion = num_uno * num_dos * num_tres
print("Multiplicacion:")
print(resultado_multiplicacion)

## Division
resultado_division = num_uno / num_dos / num_tres
print("Division:")
print(resultado_division)

## Division entera
resultado_division_entera = num_uno // num_dos // num_tres
print("Division entera:")
print(resultado_division_entera)

## Potencia
resultado_potencia = num_uno ** num_dos ** num_tres
print("Potencia:")
print(resultado_potencia)

## Combinacion
resultado_combinacion = ((num_uno + num_dos) * (num_tres - num_uno) / num_dos) // num_uno ** num_dos
print("Combinacion:")
print(resultado_combinacion)