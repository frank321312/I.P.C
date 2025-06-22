import pandas as pd

data = {
    'nombre': ['Harry Potter', 'El Señor de los Anillos', 'Barbie', 'Rapido y Furioso 18'],
    'año': [2001, 2003, 1972, 2040],
    'puntuacion': [8, 9, 8, 3]
}

df_pelis = pd.DataFrame(data)

puntaje_mayor_siete = df_pelis[df_pelis['puntuacion'] > 7]

print(puntaje_mayor_siete)