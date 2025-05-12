## a.Escribir una función que reciba una lista de nombres y un número, que representa el cupo. 
## La función debe devolver en una lista a los nombres que no pudieron entrar al curso por falta de cupo. 

def chequear_cupo(nombres: list[str], cupos: int):
    return [nombres[::-1][i] for i in range(len(nombres) - cupos)]

print(chequear_cupo(['Agustina', 'Iara', 'Priscila', 'Sol', 'Lucía', "Pepe", "Argento"], 4))

## b.Modificar la función anterior para que devuelva únicamente a la última persona de la lista de la gente que pudo entrar.
## Ejemplo: chequear_cupo(['Agustina', 'Iara', 'Priscila', 'Sol', 'Lucía'], 3) debe devolver 'Priscila', porque es la última que tuvo cupo.

def quien_recibio_el_ultimo_cupo(nombres: list[str], cupos: int):
    return nombres[cupos-1]

print(quien_recibio_el_ultimo_cupo(['Agustina', 'Iara', 'Priscila', 'Sol', 'Lucía'], 3))