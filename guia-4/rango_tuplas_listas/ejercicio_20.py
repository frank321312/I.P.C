## Se tiene una base de datos con nombres de libros de la siguiente forma ["La Noche de la Usina", "La Pregunta de sus Ojos", "Ser Feliz era Esto",...], 
## y se quiere saber cuántos libros repetidos tienen. Escribir una función que reciba la base de datos y devuelva, 
## para cada uno de los títulos, cuántos ejemplares hay. La lista no tiene un tamaño fijo, y puede contener muchos títulos repetidos.

libros = [
    "Cien años de soledad",
    "El amor en los tiempos del cólera",
    "1984",
    "Fahrenheit 451",
    "Cien años de soledad",  
    "Crimen y castigo",
    "El gran Gatsby",
    "1984",  
    "Don Quijote de la Mancha",
    "Fahrenheit 451"  
]

def copias_que_hay(libros: list):
    libros_no_repetidos = []

    for i in libros:
        i not in libros_no_repetidos and libros_no_repetidos.append(i)

    return [[i, len(list(filter(lambda x: x == i ,libros)))] for i in libros_no_repetidos]

print(copias_que_hay(libros))