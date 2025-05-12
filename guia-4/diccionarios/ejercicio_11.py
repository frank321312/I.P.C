## La profesora Llamell guarda las notas del parcial de Pensamiento Computacional en una lista de diccionarios. 
## Cada diccionario tiene la siguiente información: nombre, apellido, intento, nota.
##Los intentos pueden ser 1 (si es la primera vez que rinde el parcial) o 2 (si está en el recuperatorio).

alumnos = [
    {'nombre': 'Ana', 'apellido': 'Pérez', 'intento': 1, 'nota': 8},
    {'nombre': 'Juan', 'apellido': 'Gómez', 'intento': 2, 'nota': 6},
    {'nombre': 'Carlos', 'apellido': 'Rodríguez', 'intento': 1, 'nota': 9},
    {'nombre': 'Lucía', 'apellido': 'Martínez', 'intento': 2, 'nota': 7},
    {'nombre': 'Pedro', 'apellido': 'López', 'intento': 1, 'nota': 5},
    {'nombre': 'Marta', 'apellido': 'González', 'intento': 2, 'nota': 6},
    {'nombre': 'Santiago', 'apellido': 'Fernández', 'intento': 1, 'nota': 10},
    {'nombre': 'Isabel', 'apellido': 'Sánchez', 'intento': 2, 'nota': 4},
    {'nombre': 'Marcos', 'apellido': 'Vázquez', 'intento': 1, 'nota': 7},
    {'nombre': 'Clara', 'apellido': 'Ramírez', 'intento': 2, 'nota': 8}
]

## a.Se pide hacer una función que dada esta lista de diccionarios, se devuelva el promedio de las notas en la primera oportunidad de los alumnos.

def calcular_promedio_de_primer_intento(alumnos: list[dict] = alumnos):
    alumnos_intento_1 = [alumno["nota"] for alumno in alumnos if alumno["intento"] == 1]
    return sum(alumnos_intento_1) / len(alumnos_intento_1)

## b.Generalizar la función anterior, para que también reciba el número de intento y se pueda devolver el promedio de cualquiera de los dos intentos.

def calcular_promedio_generalizado(alumnos: list[dict] = alumnos):
    alumnos_notas = [alumno["nota"] for alumno in alumnos]
    return sum(alumnos_notas) / len(alumnos_notas)

# print(calcular_promedio_de_primer_intento())

print(calcular_promedio_generalizado())