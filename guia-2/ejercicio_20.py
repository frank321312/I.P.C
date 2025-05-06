## Como calcular el área de un rectángulo (alineado con los ejes x e y), dadas sus coordenadas x1, x2, y1 y y2.
## Considerar que tiene que funcionar para cualquier cuadrado, independientemente de los cuadrantes en los que tenga sus vértices.

def calcular_area_rectangulo_alineado_x_y(x1, x2, y1, y2):
    return abs(x2 - x1) * abs(y2 - y1)

print(calcular_area_rectangulo_alineado_x_y(3, -4, 5, -2))