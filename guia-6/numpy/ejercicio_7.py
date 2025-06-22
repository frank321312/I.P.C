import numpy as np

def devolver_ubicacion_matriz(matriz, posicion):
    return np.array(matriz)[posicion[0], posicion[1]]

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
posicion = (1, 2)

resultado = devolver_ubicacion_matriz(matriz, posicion)
print(resultado)