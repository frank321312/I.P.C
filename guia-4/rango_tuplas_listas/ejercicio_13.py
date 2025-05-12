## Se quiere crear una lista de supermercado, solicitándole al usuario productos hasta que ingrese el valor ‘X’. 
# La función debe devolver los productos en un string, separados por comas. Ejemplo: si se ingresa ‘pan’, ‘arroz’, ‘pescado’, ‘X’, debe devolver "pan, arroz, pescado".

def crear_lista_de_supermercado():
    producto = input("Ingrese el producto 'X para salir': ")
    lista = []

    while (producto != "X"):
        lista.append(producto)
        producto = input("Ingrese el producto 'X para salir': ")

    return ", ".join(lista)

print(crear_lista_de_supermercado())