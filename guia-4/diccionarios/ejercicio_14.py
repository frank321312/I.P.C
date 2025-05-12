## Laura tiene una lista de diccionarios donde guarda el valor de todas las reviews laborales anuales que le hicieron. 
## La información de cada una es año, seniority en ese momento (trainee, junior, semisenior, senior), el sueldo en ese momento y el valor del bono de performance que le dieron. 
## La semana pasada le avisaron que por políticas de la empresa, los bonos ahora deben calcularse como un porcentaje de su sueldo.

## Laura quiere entonces actualizar sus diccionarios, para que en vez de guardar el monto exacto del bono, guarde el porcentaje que le corresponde. 
## Ejemplo: si en el 2019 su sueldo era de $1.000.000 y el bono que le dieron era de $40.000, el bono fue del 4% del sueldo.

reviews = [
    {'año': 2019, 'seniority': 'junior', 'sueldo': 1000000, 'bono': 510000},
    {'año': 2020, 'seniority': 'semisenior', 'sueldo': 1200000, 'bono': 60000},
    {'año': 2021, 'seniority': 'senior', 'sueldo': 1500000, 'bono': 780000}
]

## Hacer una función que reciba la lista de diccionarios, y para cada una de las reviews, modifique el valor del bono por el porcentaje correspondiente.

def modificar_bono_por_porcentaje(reviews: list):
    return list(map(lambda x: { **x, "bono": (x["bono"] / x["sueldo"]) * 100 }, reviews))

reviews_bono = modificar_bono_por_porcentaje(reviews)

## Hacer una función que reciba la lista de diccionarios ya modificada y devuelva los años en los que Laura tuvo un bono mayor al 50% de su sueldo. Restricción: usar filter y map.

def obtener_porcentaje_mayor_a_50(reviews: list):
    return list(map(lambda x: x["año"], filter(lambda x: x["bono"] > 50, reviews)))

print(obtener_porcentaje_mayor_a_50(reviews_bono))