## Escribir una función que reciba dos vectores y devuelva su prod_escalar
## Si los vectores no tienen las mismas dimensiones, la función debe devolver None

def calcular_producto_escalar(vector1, vector2):
    if (len(vector1) != len(vector2)):
        return None

    return sum([vector1[i] * vector2[i] for i in range(len(vector1))])

print(calcular_producto_escalar([1,2,3], [4,-1,5]))