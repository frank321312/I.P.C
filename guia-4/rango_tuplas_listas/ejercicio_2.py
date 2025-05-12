## a.Una lista y devuelva True si su longitud es par y False si su longitud es impar.

def longitud_es_par_o_impar(lista: list):
    return len(lista) % 2 == 0

print(longitud_es_par_o_impar([1,2,3,4,5]))

## b.Una lista de números cualesquiera y devuelva el elemento máximo y el mínimo.

def devolver_valor_maximo_y_minimo(lista: list):
    return [min(lista), max(lista)]

print(devolver_valor_maximo_y_minimo([4,1,65,8,3]))

## c.Una lista de números y devuelva otra lista con los mismos números ordenados de menor a mayor.

def devolver_lista_ordenada(lista: list):
    return sorted(lista)

print(devolver_lista_ordenada([4,1,65,8,3]))