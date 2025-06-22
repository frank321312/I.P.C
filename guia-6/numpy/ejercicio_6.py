import numpy as np

def prod_escalar(vector_1, vector_2):
    return np.dot(vector_1, vector_2) if len(vector_1) == len(vector_2)  else None

print("Producto escalar de [1, 2, 3] y [4, 5, 6]:", prod_escalar([1, 2, 3], [4, 5, 6]))