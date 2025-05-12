## Se quiere guardar información de un grupo de maratonistas. Se necesita guardar su nombre, DNI y todas las maratones que corrió. 
## Para esto último, se guardan: nombre de cada una, año, puesto y el tiempo que tardaron en correrlas (en minutos).

## a.Crear un diccionario de ejemplo que represente esta situación.

maratonistas = {
    '12345678': {
        'nombre': 'Juan Pérez',
        'maratones': [
            {'nombre_maratón': 'Maratón de Nueva York', 'año': 2022, 'puesto': 120, 'tiempo': 180},
            {'nombre_maratón': 'Maratón de Buenos Aires', 'año': 2023, 'puesto': 5, 'tiempo': 150},
            {'nombre_maratón': 'Maratón de Londres', 'año': 2021, 'puesto': 35, 'tiempo': 160}
        ]
    },
    '23456789': {
        'nombre': 'Ana Gómez',
        'maratones': [
            {'nombre_maratón': 'Maratón de Tokio', 'año': 2022, 'puesto': 25, 'tiempo': 155},
            {'nombre_maratón': 'Maratón de Berlín', 'año': 2023, 'puesto': 10, 'tiempo': 145},
        ]
    },
    '34567890': {
        'nombre': 'Carlos Rodríguez',
        'maratones': [
            {'nombre_maratón': 'Maratón de Chicago', 'año': 2021, 'puesto': 40, 'tiempo': 170},
            {'nombre_maratón': 'Maratón de París', 'año': 2023, 'puesto': 20, 'tiempo': 160},
        ]
    }
}

## b.Teniendo esta lista de diccionarios, ordenarlos alfabéticamente por el nombre de los maratonistas.

def ordenar_maratonista_alfabeticamente(maratonistas: dict):
    return dict(sorted(maratonistas.items(), key=lambda x: x[1]["nombre"]))

## print(ordenar_maratonista_alfabeticamente(maratonistas))

## c.Teniendo esta lista de diccionarios, ordenar las maratones en tiempo ascendente según el tiempo que tardaron en correrlas.

def ordenar_maratonista_por_tiempo(maratonistas: dict):
    maratones_ordenados = []
    
    for i in [i["maratones"] for i in maratonistas.values()]:
        maratones_ordenados.append(sorted(i, key=lambda x: x["tiempo"]))
    
    for i, v in enumerate(maratonistas):
        maratonistas[v]["maratones"] = maratones_ordenados[i]
        
    return maratonistas
    

print(ordenar_maratonista_por_tiempo(maratonistas))