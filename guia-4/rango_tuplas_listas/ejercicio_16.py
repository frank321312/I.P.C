## Desafio (obligatorio): Escribir una función que reciba una matriz y devuelva su transpuesta. 
## Ejemplo: si recibe la matriz [[1, 2, 3], [4, 5, 6]], debe devolver [[1, 4], [2, 5], [3, 6]].

def devolver_transpuesta_matriz(matriz: list[list[int]]):
    # 1.Primera forma
    # lista = []

    # for i in range(len(matriz[0])):
    #     sub_lista = []

    #     for x in range(len(matriz)):
    #         print(matriz[x][i])
    #         sub_lista.append(matriz[x][i])

    #     lista.append(sub_lista)

    # return lista

    # 2.Segundo forma
    # return [[*i] for i in zip(*matriz)]
    
    # 3.Tercera forma
    return list(zip(*matriz))

print(devolver_transpuesta_matriz([[1, 2, 3], [4, 5, 6]]))