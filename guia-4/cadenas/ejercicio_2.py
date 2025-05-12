## Escribir una función que reciba una cadena que contiene un largo número entero y devuelva una cadena con el número y las separaciones de miles. 
## Por ejemplo, si recibe 1234567890, debe devolver 1.234.567.890. Cuidado: no es lo mismo 123.456.789.0 que 1.234.567.890. 
## Tienen que ser separaciones de miles y quedar un número válido.

def separacion_de_miles(numero: str):
    if (not numero.isdigit()):
        return "Debe ser un numero"

    contador = 0
    nueva_cadena = ""

    for i in range(len(numero) - 1, -1, -1):
        contador += 1
        nueva_cadena += numero[i]
        if (contador == 3):
            nueva_cadena += "."
            contador = 0

    return nueva_cadena[::-1]

print(separacion_de_miles("12345678902"))


# 1.000
# 10.000
#---------------------------
# 100.000
# 1.000.000
# 10.000.000
# 100.000.000
# 1.000.000.000
# 10.000.000.000
# 100.000.000.000
# 1.000.000.000.000