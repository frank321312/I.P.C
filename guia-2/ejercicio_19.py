## Escribir una función que calcule la norma de un vector en R3 recibiendo como parámetros las 3 componentes v1, v2 y v3 del mismo.

import math

def calcular_norma_de_un_vector_r3(v1, v2, v3):
    return math.sqrt(pow(v1, 2) + pow(v2, 2) + pow(v3, 2))

print(calcular_norma_de_un_vector_r3(2, -3, 6))