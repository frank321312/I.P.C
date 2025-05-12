productos = [
    (1, "Camiseta de algodón", 19.99),
    (2, "Pantalón deportivo", 29.95),
    (3, "Zapatos deportivos", 59.99),
    (4, "Gorra ajustable", 14.50),
    (5, "Chaqueta impermeable", 89.99)
]

productos_a_facturar = [
    (1, 2),
    (3, 1),
    (5, 3),
    (4, 1)
]

def generar_factura(productos: list[tuple], facturar: list[tuple]):
    print([(i[1], productos[i[0] - 1][1], productos[i[0] - 1][2], round(i[1] * productos[i[0] - 1][2], 2)) for i in facturar])

generar_factura(productos, productos_a_facturar)