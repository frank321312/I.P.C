## Escribir una función que dado un valor N, devuelva una lista con los números del 1 a N.

def devolver_n_numeros(n: int):
    return [*range(1, n+1)]

print(devolver_n_numeros(20))