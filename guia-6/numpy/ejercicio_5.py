import numpy as np

def es_par_el_array(arr):
    return len(arr) % 2 == 0

def valor_maximo_y_minimo(arr):
    return [np.min(arr), np.max(arr)]

def ordenar_arr(arr):
    return np.sort(arr)

# Pruebas de las funciones
arr = np.array([3, 1, 4, 1, 5, 9])

print("es_par_el_array:", es_par_el_array(arr))
print("valor_maximo_y_minimo:", valor_maximo_y_minimo(arr))
print("ordenar_arr:", ordenar_arr(arr))
