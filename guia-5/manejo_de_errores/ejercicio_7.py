# def dividir(a, b):
#     try:
#         if b == 0:
#             raise ValueError("No se puede dividir por cero")
#         return a / b
#     except ValueError as error:
#         print(error)

def dividir(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return n1/n2

def input_division():
    while True:
        try:
            n1 = int(input("Ingrese el dividendo: "))
            n2 = int(input("Ingrese el divisor: "))
            return dividir(n1, n2)
        except ValueError:
            print("Error: Debe ingresar un numero valido")
        except ZeroDivisionError as error:
            print(error)
            return None

print(input_division())