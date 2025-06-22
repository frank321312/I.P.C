import math
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * math.pi, 1000)

seno_x = np.sin(x)
coseno_x = np.cos(x)
seno_x_2 = seno_x + x / 2

fig, ax = plt.subplots()

ax.plot(x, seno_x, label='seno_x')
ax.legend()
ax.grid()
ax.set_title('Seno de x')
plt.show()

fig2, ax2 = plt.subplots()
ax2.plot(x, coseno_x, label='coseno_x')
ax2.legend()
ax2.grid()
ax2.set_title('Coseno de x')
plt.show()

fig3, ax3 = plt.subplots()
ax3.plot(x, seno_x_2, label='(seno de x) + x/2')
ax3.legend()
ax3.grid()
ax3.set_title('Operacion con seno de x')
plt.show()
