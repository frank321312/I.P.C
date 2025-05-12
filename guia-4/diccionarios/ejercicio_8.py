## Escribir una función que reciba una lista de diccionarios y una clave, y devuelva una lista con los valores correspondientes a esa clave.

productos = [
    {"producto": "Manzanas", "cantidad": 10, "precio": 1.20},
    {"producto": "Plátanos", "cantidad": 5, "precio": 0.80},
    {"producto": "Peras", "cantidad": 8, "precio": 1.50},
    {"producto": "Naranjas", "cantidad": 12, "precio": 1.00},
    {"producto": "Uvas", "cantidad": 15, "precio": 2.00},
    {"producto": "Fresas", "cantidad": 6, "precio": 2.50}
]

def valores_de_las_claves(clave, lista: list[dict] = productos):
    return [i.get(clave, None) for i in lista]

print(valores_de_las_claves("productos"))