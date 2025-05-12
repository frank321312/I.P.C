## Devuelva la primera letra de cada palabra. Ejemplo: si se recibe Ciclo Básico Común se debe devolver CBC.

def devolver_primera_letra_de_cada_palabra(cadena: str):
    nueva_cadena = ""
    for i in cadena:
        if (i.isupper()):
            nueva_cadena += i
    
    return nueva_cadena

print(devolver_primera_letra_de_cada_palabra("Ciclo Básico Común"))

## Indique si se trata de un palíndromo. Por ejemplo, anita lava la tina es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

def es_palindromo(cadena: str):
    return cadena.replace(" ", "").lower() == cadena[::-1].lower().replace(" ", "")

print(es_palindromo("Anita lava la tina"))