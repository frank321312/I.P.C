## Escribir una función que reciba dos fichas de dominó y determine si encajan o no entre sí.

## a.Resolver teniendo en cuenta que las fichas se reciben con formato de tuplas. Ejemplo: (3,4) y (5,4).
## b.Resolver teniendo en cuenta que las fichas se reciben con formato de string.

def convertir_a_tupla(ficha):
    return tuple(map(lambda x: int(x), ficha.replace("-", ""))) if isinstance(ficha, str) else ficha

def encajan_fichas(ficha1: tuple | str, ficha2: tuple | str):
    iterador1 = convertir_a_tupla(ficha1)
    iterador2 = convertir_a_tupla(ficha2)
    return any(x in iterador1 for x in iterador2)

print(encajan_fichas((3,8), (5,8)))
print(encajan_fichas("3-4", (2,5)))
print(encajan_fichas((5,4), "3-1"))
print(encajan_fichas("5-3", "3-1"))