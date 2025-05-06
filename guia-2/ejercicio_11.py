## Crear una función que reciba dos enteros y que devuelva el resto y el cociente entre ellos.

def obtener_cociente_y_resto(num1, num2):
    cociente = num1 / num2
    resto = num1 % num2
    return round(cociente, 2), resto

print(obtener_cociente_y_resto(10, 3))