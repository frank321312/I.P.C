## Escribir una función que dada la cantidad de ejercicios de un examen, y el porcentaje de ejercicios bien resueltos necesario para aprobar dicho examen, revise un grupo de exámenes. 

## Para ello, en cada paso debe preguntarle al usuario la cantidad de ejercicios resueltos por el alumno, o pedirle que ingrese “*” para salir. Debe mostrar por pantalla el porcentaje correspondiente a la cantidad de ejercicios resueltos respecto a la cantidad de ejercicios del examen y una leyenda que indique si aprobó o no.

## Adicional al punto anterior: imprimir un mensaje informándole al usuario la cantidad de ejercicios y el % de aprobación.

## Validar que el usuario siempre ingrese números positivos y menor o iguales a la cantidad de ejercicios del examen, o “*“. De lo contrario, mostrar un mensaje de error y volver a pedirle el dato al usuario.

def revisar_examenes(cantidad_examen, cantidad_ejercicios):
    resolvio = input("Ingrese la cantidad de ejercicios que resolvió ('*' para salir): ")
    while (resolvio != "*" and cantidad_examen > 1):
        if (resolvio.isnumeric() and int(resolvio) <= cantidad_ejercicios and int(resolvio) >= 0):
            cantidad_examen -= 1
            porcentaje = (int(resolvio) / cantidad_ejercicios) * 100
            print(f"Cantidad de ejercicios: {cantidad_ejercicios}")
            print(f"Porcentaje de aprobacion: {porcentaje}%")
            print("Aprobado") if porcentaje >= 60 else print("Desaprobado")
        else:
            print("Error, vuelva a ingresar los datos")

        resolvio = input("Ingrese la cantidad de ejercicios que resolvió ('*' para salir): ")

revisar_examenes(3, 10)