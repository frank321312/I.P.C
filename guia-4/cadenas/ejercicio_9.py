## Escribir una función que reciba dos cadenas de caracteres y devuelva una lista con todos los caracteres que no tienen en común. 
## Ejemplo: 'Python' y 'Hola' debería devolver el conjunto de letras ['P', 'y', 't', 'l', 'a', 'n'], indiferentemente del orden y de si está en mayúscula o minúscula.

def devolver_caracter_no_coincidentes(cadena1: str, cadena2: str):
    lista = []
    concatenar = cadena1 + cadena2
    for i in concatenar:
        if (concatenar.lower().count(i.lower()) == 1):
            lista.append(i)

    return lista

print(devolver_caracter_no_coincidentes("Python", "Hola"))