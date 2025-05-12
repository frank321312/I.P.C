## a.Un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe 
## "Que lindo dia que hace hoy" debe devolver: {'que': 2, 'lindo': 1, 'dia': 1, 'hace': 1, 'hoy': 1}.
## b.Un diccionario con la cantidad de apariciones de cada caracter en la cadena.

def cantidad_de_palabras(cadena: str):
    diccionario = {}
    diccionario_caracter = {}

    for i in cadena.lower().split(" "):
        if (i in diccionario):
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    
    for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        diccionario_caracter[i] = cadena.count(i)

    diccionario_caracter = dict(filter(lambda x: x[1] > 0, diccionario_caracter.items()))

    print(diccionario_caracter)
    return diccionario

print(cantidad_de_palabras("Que lindo dia que hace hoy"))
