## Se tiene un ticket de supermercado en forma de diccionario con los siguientes datos:
## Nombre del Producto
## Precio por Unidad
## Cantidad
## Se pide hacer una función que reciba el ticket y devuelva el monto a pagar total.

ticket_supermercado = [
    {"nombre_producto": "Manzanas", "precio_por_unidad": 1.20, "cantidad": 10},
    {"nombre_producto": "Plátanos", "precio_por_unidad": 0.80, "cantidad": 5},
    {"nombre_producto": "Peras", "precio_por_unidad": 1.50, "cantidad": 8},
    {"nombre_producto": "Naranjas", "precio_por_unidad": 1.00, "cantidad": 12},
    {"nombre_producto": "Uvas", "precio_por_unidad": 2.00, "cantidad": 15},
    {"nombre_producto": "Fresas", "precio_por_unidad": 2.50, "cantidad": 6}
]

def monto_a_pagar(ticket: list[dict] = ticket_supermercado):
    return sum(map(lambda x: x["precio_por_unidad"] * x["cantidad"], ticket))

print(monto_a_pagar())