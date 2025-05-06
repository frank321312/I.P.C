##Escribir una implementación propia de la función abs, que devuelva el valor absoluto de cualquier valor que reciba.

def mi_abs(n):
    return n if n >= 0 else n + n * -2

print(mi_abs(4))