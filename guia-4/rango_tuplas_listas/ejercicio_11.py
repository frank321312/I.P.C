## Escribir una función que reciba una matriz y una tupla (fila, columna), y devuelva el valor ubicado en esa posición de la matriz. 

def devolver_posicion_matriz(matriz, tupla):
    return matriz[tupla[0]][tupla[1]]

print(devolver_posicion_matriz([[1, 2], [3, 4]], (0,1)))