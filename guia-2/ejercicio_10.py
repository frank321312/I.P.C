## Crear una función que reciba un número y un string, y que devuelva ambos concatenados dentro de un nuevo string.

def concatenar(numero, texto: str):
    return str(numero) + texto

print(concatenar(5, " es un número"))