## Escribir un programa que le pida al usuario que ingrese un número. Para ese número, se imprime la tabla de multiplicar del 1 al 10. Luego, se le vuelve a pedir otro número. Si el usuario ingresa “X”, el programa debe terminar. El usuario debe poder ingresar números indefinidamente hasta que ingrese “X”. 

from ejercicio_2 import mostrar_tablas_para

def mostrar_tablas_hasta():
    n = input("Ingrese un número o 'X' para salir: ")
    
    while (n != "X"):

        if (n in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]):
            mostrar_tablas_para(int(n))
            n = input("Ingrese un número o 'X' para salir: ")
        else:
            print("El número debe ser un entero entre 1 y 10.")
            n = input("Ingrese un número o 'X' para salir: ")

mostrar_tablas_hasta()