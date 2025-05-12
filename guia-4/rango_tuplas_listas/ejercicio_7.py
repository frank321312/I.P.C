## a.Escribir una función que reciba una tupla, un índice, y un nuevo valor. 
## La función debe modificar la tupla, cambiando el valor en la posición dada por el índice, por el nuevo valor pasado como parámetro. Devolver la tupla modificada.

def reemplazar_valor_por_indice_tupla(tupla, indice, valor):
    return (*tupla[:indice], valor, *tupla[indice + 1:])

print(reemplazar_valor_por_indice_tupla((1,2,3,4,5,6), 2, "Milanesa"))

## b.Repetir el ejercicio anterior, pero con una lista.

def reemplazar_valor_por_indice_lista(lista, indice, valor):
    return [*lista[:indice], valor, *lista[indice + 1:]]

print(reemplazar_valor_por_indice_lista([1,2,3,4,5,6], 2, "Milanesa"))

## Repetir ambos si ahora, en vez de recibir un índice, se recibe el valor a eliminar. Si no se contiene al valor, se devuelve la estructura tal cual se recibió.

def eliminar_por_valor_tupla(tupla: tuple, valor):
    if (valor not in tupla):
        return tupla
    
    indice = tupla.index(valor)
    return (*tupla[:indice], *tupla[indice + 1:])

print(eliminar_por_valor_tupla((1,2,3,4,5,6), 2))

def eliminar_por_valor_lista(lista: tuple, valor):
    if (valor not in lista):
        return lista
    
    indice = lista.index(valor)
    return [*lista[:indice], *lista[indice + 1:]]

print(eliminar_por_valor_lista((1,2,3,4,5,6), 2))