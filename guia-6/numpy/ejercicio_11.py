import numpy as np

def matriz_de_asientos(lista, filas, columnas):
    return np.reshape(lista, (filas, columnas)) if len(lista) == filas * columnas else None

asientos = [1,2,3,0,7,6,4,0,0,8,9,10,0,13,11,12]

matriz = matriz_de_asientos(asientos, 4, 4)
print(matriz)