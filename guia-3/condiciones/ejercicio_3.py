## Escribir una función que reciba un número y devuelva True si es entero y False si no lo es.

def es_entero(n):
    return type(n) == int

print(es_entero(5)) # -> True
print(es_entero("dsadwqdw")) # -> False