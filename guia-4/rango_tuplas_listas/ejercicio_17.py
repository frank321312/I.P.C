## Escribir una función que reciba una cadena a buscar y una lista de tuplas (nombre_completo, telefono), y busque dentro de la lista todas las entradas que contengan en el 
## nombre completo la cadena recibida (puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos). Debe devolver una lista con todas las tuplas encontradas.

def buscador(lista: list[tuple[str, int]], cadena: str):
    resultados = []

    for i in lista:
        cadena.lower() in i[0].lower() and resultados.append(i)

    return resultados

print(buscador([("Juan Gonzales", 25), ("Ana", 30), ("Carlos Gonzales", 22), ("Laura", 28), ("Pedro", 35)], "gonzales"))