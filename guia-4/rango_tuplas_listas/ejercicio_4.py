## Dada la lista de tuplas [("Argentina", 3), ("España",1), ("Uruguay", 2), ("Francia",2)],
## donde cada tupla contiene un país y la cantidad de mundiales que ganaron:

## a.Hacer una función que reciba la lista por parámetro e imprima la información de cada país con el siguiente formato:

paises = [("Argentina", 3), ("España",1), ("Uruguay", 2), ("Francia",2)]

def mostrar_paises(paises = paises):
    for i in paises:
        if (i[0] == "Argentina"):
            print("Argentina⭐⭐⭐")
        else:
            print(f"País: {i[0]} - Copas: {i[1]}")

mostrar_paises()

## b.Hacer una función que reciba la lista por parámetro y devuelva la cantidad de mundiales que ganaron entre todos los países.
## Ejemplo: contar_mundiales([("Argentina", 3), ("España",1), ("Uruguay", 2), ("Francia",2)]) debe devolver 8.

def contar_mundiales(paises: list[tuple] = paises):
    return sum(map(lambda x: x[1], paises))

print(contar_mundiales())

## c.Hacer una función que reciba la lista por parámetro y la devuelva, ordenada por cantidad de copas ganadas.

def ordenar_lista_por_mundiales(paises: list[tuple] = paises):
    return sorted(paises, key=lambda x: x[1])

print(ordenar_lista_por_mundiales())

## d.Hacer una función que reciba la lista por parámetro y devuelva en una tupla: una lista con los países que tienen más de una copa ganada,
## y otra lista con valores booleanos que nos diga si la cantidad de copas es par o impar.

def devolver_tupla_por_impar_y_par(paises: list[tuple] = paises):
    paiese_con_mas_de_1_mundial = list(filter(lambda x: x[1] > 1, paises))
    return (paiese_con_mas_de_1_mundial, list(map(lambda x: x[1] % 2 == 0, paiese_con_mas_de_1_mundial)))

print(devolver_tupla_por_impar_y_par())
