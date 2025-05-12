## a.Imprimir los números del 10 al 50 inclusive, saltando de 5 en 5.

def imprimir_numeros_de_10_a_50():
    for i in range(10, 51, 5):
        print(i)

# imprimir_numeros_de_10_a_50()

## b.Imprimir los números del 40 al 20 en orden decreciente, saltando de 2 en 2.

def imprimir_numeros_de_20_a_40_decreciente():
    for i in range(40, 19, -2):
        print(i)

# imprimir_numeros_de_20_a_40_decreciente()

## c.Crear una lista con los números del 4 al 10. Luego, acceder con el índice a los elementos que contienen a los números 4, 6 y 9 e impimirlos por pantalla.

def imprimir_indice_de_4_6_9():
    lista = [*range(4, 11)]
    lista_index = [i for i, v in enumerate(lista) if v in [4,6,9]]    
    print(lista_index)

# imprimir_indice_de_4_6_9()