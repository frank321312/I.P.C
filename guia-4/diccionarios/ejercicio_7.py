## En un vivero se guardan las plantas en una lista de diccionarios con la siguiente información: especie, luz directa (si/no), precio. 
## Se necesita un sistema que guarde las plantas a medida que van llegando. Hacer una función que reciba la lista de diccionarios de plantas, 
## y los datos de la planta nueva, y agregue esa planta a la lista de diccionarios.

plantas = [
    {"especie": "Cactus", "luz_directa": "sí", "precio": 15.50},
    {"especie": "Ficus", "luz_directa": "no", "precio": 22.30},
    {"especie": "Aloe Vera", "luz_directa": "sí", "precio": 12.00},
    {"especie": "Helecho", "luz_directa": "no", "precio": 9.75},
    {"especie": "Orquídea", "luz_directa": "sí", "precio": 18.20},
    {"especie": "Pothos", "luz_directa": "no", "precio": 7.40},
    {"especie": "Suculenta", "luz_directa": "sí", "precio": 10.00}
]

def agregar_planta(nueva_planta, plantas: list = plantas):
    plantas.append(nueva_planta)

agregar_planta({"especie": "Bamboo", "luz_directa": "sí", "precio": 8.00})