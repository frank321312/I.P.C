## Escribir una función que reciba una lista y un número N. 
## Para dicho número N, debe imprimir los últimos N elementos de la lista en orden inverso, y luego devolver la lista sin ellos. 

def devolver_n_elementos(lista: list, n: int):
    print(lista[-n:][::-1])
    return lista[:-n]

print(devolver_n_elementos([1,2,3,4,5], 2))