## Escribir una función que reciba un texto y para cada caracter presente en el texto, devuelva la palabra más larga en la que se encuentra ese caracter.

def caracter_mas_largo(cadena: str):
    diccionario = {}

    for i in list(cadena.replace(" ", "")):
        contador = 0
        for palabra in cadena.split(" "):
            if (palabra.count(i) > contador):
                contador = palabra.count(i)
                diccionario[i] = palabra

    return diccionario

print(caracter_mas_largo("Este es un texto de prueba de dedalo dededededededede sarasa"))
