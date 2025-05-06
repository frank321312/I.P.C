## a.Dado un año, que devuelva si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

## b.Dado un mes y un año, que devuelva la cantidad de días correspondientes.

## c.Pedirle al usuario su día y mes de cumpleaños. El programa debe imprimir un mensaje indicando a qué signo corresponde el usuario.

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def cantidad_dias(anio, mes):
    if mes == 2:
        return 29 if es_bisiesto(anio) else 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    else:
        return 31

def signo_correspondiente():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))

    if (dia > cantidad_dias(2025, mes) or dia < 1):
        print("Día no válido")
        return

    if (mes == 1 and dia <= 20):
        print("Capricornio: 22 de diciembre al 20 de enero.")
    elif (mes == 1 and dia > 20 or mes == 2 and dia <= 19):
        print("Acuario: 21 de enero al 19 de febrero.")
    elif (mes == 2 and dia > 19 or mes == 3 and dia <= 20):
        print("Piscis: 20 de febrero al 20 de marzo.")
    elif (mes == 3 and dia > 20 or mes == 4 and dia <= 20):
        print("Aries: 21 de marzo al 20 de abril.")
    elif (mes == 4 and dia > 20 or mes == 5 and dia <= 21):
        print("Tauro: 21 de abril al 21 de mayo.")
    elif (mes == 5 and dia > 21 or mes == 6 and dia <= 21):
        print("Géminis: 22 de mayo al 21 de junio.")
    elif (mes == 6 and dia > 21 or mes == 7 and dia <= 23):
        print("Cáncer: 22 de junio al 23 de julio.")
    elif (mes == 7 and dia > 23 or mes == 8 and dia <= 23):
        print("Leo: 24 de julio al 23 de agosto.")
    elif (mes == 8 and dia > 23 or mes == 9 and dia <= 23):
        print("Virgo: 24 de agosto al 23 de septiembre.")
    elif (mes == 9 and dia > 23 or mes == 10 and dia <= 23):
        print("Libra: 24 de septiembre al 23 de octubre.")
    elif (mes == 10 and dia > 23 or mes == 11 and dia <= 22):
        print("Escorpio: 24 de octubre al 22 de noviembre.")
    elif (mes == 11 and dia > 22 or mes == 12 and dia <= 22):
        print("Sagitario: 23 de noviembre al 21 de diciembre.")
    elif (mes == 12 and dia > 22 or mes == 1 and dia <= 20):
        print("Capricornio: 22 de diciembre al 20 de enero.")
    else:
        print("Mes no válido, ingrese un mes entre 1 y 12")

signo_correspondiente()