## Desafio (obligatorio): Escribir una función que reciba un tamaño y devuelva una matriz con 1 en la diagonal principal y 0 en el resto. 
## Ejemplo: si recibe 4, debe devolver la matriz identidad de tamaño 4x4.

def crear_matriz_por_n(n: int):
    return [[*map(lambda x: 1 if x == i else 0, range(n))] for i in range(n)]

print(crear_matriz_por_n(4))