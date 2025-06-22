import pandas as pd

data = {
    'nombre': ['Violeta', 'Carla', 'Manuela'],
    'apellido': ['Perez', 'Guanca', 'Gomez'],
    'dni': [42000000, 42001001, 42002002],
    'carrera': ['Informática', 'Mecánica', 'Química'],
    'nota': [7, 4, 6],
    'intento': [1, 2, 1]
}

df = pd.DataFrame(data)

promedio = df[df['intento'] == 1]['nota'].mean()

print(promedio)