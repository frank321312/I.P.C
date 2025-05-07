## Suponiendo que el primer día del año fue lunes, escribir una función que reciba un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo: si se recibe ‘3’, debe devolver “miércoles”, y si se recibe ‘9’, debe devolver “martes”.

def devolver_dia_del_anio(dia):
    if (dia < 1 or dia > 366):
        print("Dia invalido")
        return

    if (dia % 7 == 1):
        print("Lunes")
    elif (dia % 7 == 2):
        print("Martes")
    elif (dia % 7 == 3):
        print("Miercoles")
    elif (dia % 7 == 4):
        print("Jueves")
    elif (dia % 7 == 5):
        print("Viernes")
    elif (dia % 7 == 6):
        print("Sabado")
    else:
        print("Domingo")

devolver_dia_del_anio(9)