## Escribir una función que reciba la cadena de caracteres de los productos de supermercado y devuelva una lista con cada uno de los productos por separado

def convertir_cadena_a_lista(cadena: str):
    return cadena.split(", ")

print(convertir_cadena_a_lista("pan, arroz, pescado, jugo, fideos"))

## Se tiene además otra cadena de caracteres con los precios de cada producto: "100, 50, 200, 80, 30,...". Escribir una función que reciba ambas cadenas y 
## devuelva una lista con tuplas de (producto, precio): [('pan', 100), ('arroz', 50), ('pescado', 200), ('jugo', 80), ('fideos', 30), ...].

def convertir_cadena_a_lista_con_tuplas(nombres: str, precios: str):
    return [(n, int(p)) for n, p in zip(convertir_cadena_a_lista(nombres), convertir_cadena_a_lista(precios))]

lista_de_compras = convertir_cadena_a_lista_con_tuplas("pan, arroz, pescado, jugo, fideos", "100, 50, 200, 80, 30")
print(lista_de_compras)

## Para la función del punto anterior, escribir otra función que reciba la lista de tuplas y devuelva el precio total de la lista de compras.

def calcular_precio_total(lista: list[tuple]):
    return sum(map(lambda x: x[1], lista))

print(calcular_precio_total(lista_de_compras))