## Crear un programa que le solicite al usuario 5 enteros y que muestre por pantalla el promedio de ellos. Hacerlo de dos formas:
## Primero, usando 5 variables para cada entero.
## Después, usando una sola variable para almacenar la suma de los 5 enteros.

num_uno = int(input("Ingresa el primer numero: "))
num_dos = int(input("Ingresa el segundo numero: "))
num_tres = int(input("Ingresa el tercer numero: "))
num_cuatro = int(input("Ingresa el cuarto numero: "))
num_cinco = int(input("Ingresa el quinto numero: "))

promedio = (num_uno + num_dos + num_tres + num_cuatro + num_cinco) / 5
print(f"El promedio de los 5 numeros es: {round(promedio, 2)}")