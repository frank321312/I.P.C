## Rosita tiene una lista de diccionarios donde guarda todas las películas que vió. La información para cada una es: el nombre de la película, año en que salió, y la puntuación que le puso del 1 al 10. 
## Hacer una función que reciba el diccionario y devuelva una nueva lista de diccionarios donde sólo estén las películas que tienen puntaje mayor a 7.

peliculas = [
    {'nombre': 'The Shawshank Redemption', 'año': 1994, 'puntuacion': 10},
    {'nombre': 'The Godfather', 'año': 1972, 'puntuacion': 3},
    {'nombre': 'The Dark Knight', 'año': 2008, 'puntuacion': 7},
    {'nombre': 'Pulp Fiction', 'año': 1994, 'puntuacion': 8},
    {'nombre': 'The Lord of the Rings: The Return of the King', 'año': 2003, 'puntuacion': 6},
    {'nombre': 'Forrest Gump', 'año': 1994, 'puntuacion': 9},
    {'nombre': 'Inception', 'año': 2010, 'puntuacion': 4},
    {'nombre': 'Fight Club', 'año': 1999, 'puntuacion': 8},
    {'nombre': 'The Matrix', 'año': 1999, 'puntuacion': 5},
    {'nombre': 'The Empire Strikes Back', 'año': 1980, 'puntuacion': 10}
]

## a.Resolver sin usar filter

def peliculas_mayores_a_7(peliculas = peliculas):
    return [i for i in peliculas if i["puntuacion"] > 7]

## b.Resolver usando filter.

def peliculas_mayores_a_7_con_filter(peliculas = peliculas):            
    return list(filter(lambda x: x["puntuacion"] > 7, peliculas))

print(peliculas_mayores_a_7())

# print(peliculas_mayores_a_7_con_filter())