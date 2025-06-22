import numpy as np

def crear_array():
    array = np.linspace(0, 10, num=20)
    print(array)
    print(f"Dimensiones del array: {array.ndim}")
    print(f"Forma del array: {array.shape}")
    print(f"Tamaño del array: {array.size}")

crear_array()

print(np.array([[1, 2, 3, 4], [4, 5, 6, 4], [7, 8, 9, 4], [10, 11, 12, 4]]).shape)