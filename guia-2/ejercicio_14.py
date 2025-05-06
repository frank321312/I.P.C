## Hacer una función que reciba una palabra y que imprima los primeros 5 caracteres únicamente. Ejemplo: Si se recibe “pensamiento” se debe imprimir “pensa”.

def mostrar_primeros_cinco_caracteres(texto):
    print(texto[:5])

## Hacer una función que reciba una palabra y que imprima sólo los caracteres ubicados en posiciones pares. Ejemplo: Si se recibe “pensamiento” se debe imprimir “pnaino”.

def mostrar_caracteres_par(texto):
    print(texto[::2])

## Hacer una función que reciba una palabra y que imprima la palabra dada vuelta. Ejemplo: Si se recibe “materia” se debe imprimir “airetam”.

def invertir_texto(texto):
    print(texto[::-1])

mostrar_primeros_cinco_caracteres("pensamiento")
mostrar_caracteres_par("pensamiento")
invertir_texto("materia")