## Escribir una función que, dada una cadena de caracteres, devuelva una lista con cada uno de los caracteres que la componen en mayúscula.

def devolver_cadena_a_lista_mayuscula(cadena: str):
    return list(cadena.upper())

print(devolver_cadena_a_lista_mayuscula("Hola"))