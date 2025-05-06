## Escribir un programa que le pida al usuario su año de nacimiento, y que le diga qué edad tiene en el año actual.

anio_actual = 2025
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = anio_actual - anio_nacimiento
print(f"Tu edad es: {edad} años")