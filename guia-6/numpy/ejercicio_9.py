import numpy as np

def devolver_transpuesta(matriz):
    return np.transpose(matriz)

matriz = np.array([[1, 2, 3], [4, 5, 6]])
resultado = devolver_transpuesta(matriz)
print(resultado)