## Escribir una función que, dada una cadena de caracteres, devuelva una tupla con cada uno de los caracteres que no es una vocal. Ejemplo: 'Algoritmos' debe devolver ('l', 'g', 'r', 't', 'm', 's'). 
## Restricción: no se permite el uso de ciclos for/while.

def convertir_a_tupla_solo_consonante(cadena: str):
    return tuple(filter(lambda x: x.lower() not in "aeiuo", cadena))

print(convertir_a_tupla_solo_consonante("AlgoRitmos"))