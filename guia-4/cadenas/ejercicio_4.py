## Indique si la segunda cadena es subcadena de la primera. Por ejemplo, 'compu' es subcadena de 'computacional'.

def es_subcadena(cadena: str, subcadena: str):
    return True if cadena.find(subcadena) >= 0 else False

print(es_subcadena("computacional", "sappe"))

## Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome' debe devolver 'gnome'.

def orden_alfabetico(cadena1: str, cadena2: str):
    return min(cadena1, cadena2)

print(orden_alfabetico("kde", "gnome"))