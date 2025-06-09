def es_par_o_impar():
    numero = input("Ingrese un número ('*' para salir): ")
    while (numero != "*"):
        try:
            converir_numero = int(numero)
            if converir_numero % 2 == 0:
                print(f"{numero} es par.")
            else:
                print(f"{numero} es impar.")
            numero = input("Ingrese un número ('*' para salir): ")
        except ValueError:
            print("Error, debe ingresar un número.")
            numero = input("Ingrese un número ('*' para salir): ")
            
es_par_o_impar()