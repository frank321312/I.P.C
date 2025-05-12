## Crear un diccionario que sirva para representar a cada persona. Debe contener las claves nombre, apellido, dni y carrera. Los diccionarios se deben guardan en una lista llamada estudiantes.

## Agregar al diccionario creado un nuevo elemento, que debe ser otro diccionario y represente las notas obtenidas en la carrera. La clave debe ser el codigo y el valor la nota (del 1 al 10) obtenida.

## Crear código que agregue para la estudiante Violeta Perez la nota 7 en la materia Algoritmos y Programación III (7507), y la nota 4 en la materia Análisis Matemático II (6103).
 
## Teniendo la lista de estudiantes, buscar en la lista la persona con mayor cantidad de notas e imprimirla por pantalla.

estudiantes = [
        {"nombre": "Violeta", "apellido": "Perez", "dni": 42000000, "carrera": "Informática", "codigo": []},
        {"nombre": "Carla", "apellido": "Guanca", "dni": 42001001, "carrera": "Mecánica", "codigo": []},
        {"nombre": "Manuela", "apellido": "Gomez", "dni": 42002002, "carrera": "Quimica", "codigo": []},
    ]

def agregar_nota_a(dni: int, codigo_materia: int, nota, estudiantes):
    notas_estudiantes = []

    if (nota < 1 or nota > 10):
        print("La nota debe estar entre 1 y 10")
        return

    for estudiante in estudiantes:
        if (estudiante["dni"] == dni):
            estudiante["codigo"] += [{ codigo_materia: nota }]

        notas_estudiantes.append(estudiante)

    estudiantes = notas_estudiantes

def obtener_estudiante_con_mayor_cantidad_nota(estudiantes):
    if (len(estudiantes) == 0):
        print("No hay estudiantes")
        return

    estudiante_con_mayor_cantidad = estudiantes[0]

    for estudiante in estudiantes:
        if (len(estudiante["codigo"]) > len(estudiante_con_mayor_cantidad["codigo"])):
            estudiante_con_mayor_cantidad = estudiante
    
    if (len(estudiante_con_mayor_cantidad["codigo"]) == 0):
        print("No hay estudiantes con una cantidad de notas mayor a 0")
        return

    print(estudiante_con_mayor_cantidad)
    
agregar_nota_a(42000000, 7507, 7, estudiantes)
agregar_nota_a(42000000, 6103, 4, estudiantes)

obtener_estudiante_con_mayor_cantidad_nota(estudiantes)