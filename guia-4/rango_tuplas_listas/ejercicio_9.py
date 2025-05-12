## Escribir una función que reciba una lista de números y devuelva la misma lista en orden inverso.

def invertir_orden(lista: list[int]):
    return lista[::-1]

print(invertir_orden([1,2,3,4,5,6,7,8,9,0]))