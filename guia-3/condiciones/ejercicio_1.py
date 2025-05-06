## Escribir una función que, dado un número entero m , calcule si es impar o no.

def es_impar(n):
    return "Es impar" if(n % 2 != 0) else "Es par"

print(es_impar(2))