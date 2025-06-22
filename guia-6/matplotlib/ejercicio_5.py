import numpy as np
import matplotlib.pyplot as plt

def calcular_energia_elastica(n):
    k = 0.15
    x = np.arange(0, n + 0.5, 0.5)
    energia = 1/2 * k * x**2
    return x, energia

x, y = calcular_energia_elastica(10)

fig, ax = plt.subplots()

ax.plot(x, y, label='0.15')
ax.set_title('Energía Potencial Elástica')
ax.set_xlabel('Estiramiento (m)')
ax.set_ylabel('Energía (J)')
ax.legend()
ax.grid()

plt.show()
