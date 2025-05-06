## Hacer una funcion que reciba una palabra, le borre todas las letras “a” e imprima el resultado por 
## pantalla. Pista: usar una función predefinida de Python. Ejemplo: Si se recibe “casa” se debe imprimir “cs”.

def quitar_caracter(texto: str):
    print(texto.replace("a", ""))

quitar_caracter("casa")