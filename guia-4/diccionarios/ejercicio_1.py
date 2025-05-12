## Escribir una función que reciba una lista de tuplas, 
## y que devuelva un diccionario en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos.

def tuplas_a_diccionario(lista: list):
    diccionario = {}

    for i in lista:
        if (i[0] in diccionario):
            diccionario[i[0]] += [i[1]]
        else:
            diccionario[i[0]] = [i[1]]
    
    return diccionario

l = [('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días')]
print(tuplas_a_diccionario(l))