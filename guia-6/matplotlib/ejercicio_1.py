import matplotlib.pyplot as plt
import numpy as np

x = np.arange(101)

y = x**2

z = 3*x + 2

q = 1/(x+1)

e = np.log10(x + 1)

fig, ax = plt.subplots()

ax.plot(x, y, label='x^2')
ax.plot(x, z, label='3*x+2')
ax.plot(x, q, label='1/(x+1)')
ax.plot(x, e, label='log10(x + 1)')

ax.set_title("Gráfico de múltiples curvas")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid()
ax.legend()
plt.show()

fig2, ax2 = plt.subplots()
ax2.plot(x, q, label="1 / (x + 1)")
ax2.plot(x, e, label="log10(x)")
ax2.set_title("Funciones con valores pequeños en eje Y")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.legend()
ax2.grid(True)
plt.show()