## Hacer una función que reciba una lista de palabras, las ordene en orden alfabético y luego las una en un string separadas por espacios. 
## Ejemplo: si recibe ['hola', 'como', 'estas'], debe devolver "como estas hola".

def ordenar_lista_de_palabras(lista: list[str]):
    return " ".join(sorted(lista))

print(ordenar_lista_de_palabras(['hola', 'como', 'estas']))