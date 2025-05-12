## En una fábrica se tiene una base de datos donde se guardan todos los códigos de los productos que se fabrican como claves de un diccionario. 
## Los valores de cada clave son nuevos diccionarios, con la siguiente información: fecha de vencimiento (mes,año), si pasó el chequeo de calidad o no.
## Se pude hacer una función que reciba esta lista de diccinoarios, y elimine a todos los productos que no pasaron el chequeo de calidad. 
## Devolver en una tuple todos los productos eliminados en formato {codigo: diccionario del producto}.

productos = {
    'P001': {'fecha_vencimiento': (12, 2025), 'paso_calidad': True},
    'P002': {'fecha_vencimiento': (5, 2024), 'paso_calidad': False},
    'P003': {'fecha_vencimiento': (10, 2023), 'paso_calidad': True},
    'P004': {'fecha_vencimiento': (7, 2026), 'paso_calidad': True},
    'P005': {'fecha_vencimiento': (3, 2025), 'paso_calidad': False},
    'P006': {'fecha_vencimiento': (11, 2024), 'paso_calidad': True},
    'P007': {'fecha_vencimiento': (8, 2023), 'paso_calidad': False},
    'P008': {'fecha_vencimiento': (6, 2027), 'paso_calidad': True}
}

def eliminar_productos_de_mala_calidad(lista_productos: dict = productos):
    productos_de_calidad = dict(filter(lambda x: x[1]["paso_calidad"] == True, lista_productos.items()))
    productos_de_mala_calidad = tuple(filter(lambda x: x[1]["paso_calidad"] == False, lista_productos.items()))
    return { "calidad": productos_de_calidad, "mala_calidad": productos_de_mala_calidad }

print(eliminar_productos_de_mala_calidad())