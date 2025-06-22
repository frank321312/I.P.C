import numpy as np
import matplotlib.pyplot as plt

def calcular_posicion_final_de_movil(posicion_inicial, velocidad_inicial, tiempo, aceleracion):
    x = posicion_inicial + velocidad_inicial * tiempo + 1/2 * aceleracion * tiempo**2
    return x

valores_tiempo = np.linspace(0, 100, 5000)

movil_1 = calcular_posicion_final_de_movil(0, 0, valores_tiempo, 1)
movil_2 = calcular_posicion_final_de_movil(500, 4, valores_tiempo, 0.5)

fig, ax = plt.subplots()
ax.plot(valores_tiempo, movil_1, label='posicion: 0')
ax.plot(valores_tiempo, movil_2, label='posicion: 500')
ax.legend()
ax.grid()
ax.set_title('Posición de dos móviles en función del tiempo')
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Posición (m)')
plt.show()