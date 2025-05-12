## Se quiere implementar un buscador dentro de un editor de texto, que permita encontrar todas las ocurrencias de una palabra en un texto. 
## Para ello, se debe implementar una función que reciba como parámetro una palabra y un texto, y que devuelva la primer aparición de la palabra en el texto.

def devolver_primera_aparicion(buscar: str, texto: str):
    return texto.find(buscar)

print(devolver_primera_aparicion("al", "calcule el precio al valor actual"))

## Modificar la función anterior para que devuelva una lista con las posiciones de inicio de cada ocurrencia de la palabra dentro del texto. 
## Ejemplo: si se busca 'al' en 'calcule el precio al valor actual', debe devolver [1, 18, 22, 31].

def devolver_todas_las_apariciones(buscar: str, texto: str):
    lista = []

    for i in range(texto.count(buscar)):
        lista.append(texto.find(buscar) if len(lista) == 0 else texto.find(buscar, lista[i - 1] + 1))

    return lista

print(devolver_todas_las_apariciones("al", "calcule el precio al valor actual"))

## Modificar la función anterior para que devuelva la cantidad de ocurrencias encontradas. Ejemplo: si se busca 'al' en 'calcule el precio al valor actual', debe devolver 4.

def devolver_cantidad_de_veces_encontrada(buscar: str, texto: str):
    return texto.count(buscar)

print(devolver_cantidad_de_veces_encontrada("al", "calcule el precio al valor actual"))