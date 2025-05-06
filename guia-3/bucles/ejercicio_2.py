## Se quiere hacer un programa para enseñar a los niños las tablas de multiplicar del 1 al 10. Crear una función que reciba un número e imprima por pantalla la tabla de multiplicar de ese número.

def mostrar_tablas_para(n):
    if (not isinstance(n, int) or n < 1 or n > 10):
        print("El número debe ser un entero entre 1 y 10.")
        return

    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# mostrar_tablas_para(5)