import numpy as np

def crear_array():
    arr = np.arange(0, 10)
    arr_2 = arr.reshape(2, 5)
    arr_3 = np.insert(arr, 3, 100)
    
    print(f"Array original: {arr}")
    print(f"Array 2D: {arr_2}")
    print(f"Array con elemento insertado: {arr_3}")
    
crear_array()