import matplotlib.pyplot as plt
import numpy as np

años = np.arange(2012, 2022)

ventas = [140, 60, 120, 250, 200, 180, 100, 300, 120, 160]
ganancias = [14000, 45000, 20400, 100000, 50000, 25000, 100000, 30000, 15000, 35000]
productos = ["prod_1", "prod_2", "prod_3", "prod_4", "prod_5", "prod_6", "prod_7", "prod_8", "prod_9", "prod_10"]
cant_ventas_productos_2024 = [180, 160, 190, 140, 100, 200, 120, 130, 150, 170]

## Punto A
# fig, ax = plt.subplots()

# ax.bar(años, ventas)
# ax.set_xlabel('Años')
# ax.set_ylabel('Ventas')
# ax.set_title('Grafico ventas 2012-2022')

# plt.show()

## Mejor para este punto
# fig2, ax2 = plt.subplots()

# ax2.plot(años, ventas)
# ax2.set_xlabel('Años')
# ax2.set_ylabel('Ventas')
# ax2.set_title('Grafico ventas 2012-2022')
# ax2.grid()
# plt.show()

# fig, ax = plt.subplots()

# ax.bar(años, ganancias)
# ax.set_xlabel('Años')
# ax.set_ylabel('Ventas')
# ax.set_title('Grafico ventas 2012-2022')

# plt.show()

# fig2, ax2 = plt.subplots()

# ax2.plot(años, ganancias)
# ax2.set_xlabel('Años')
# ax2.set_ylabel('Ventas')
# ax2.set_title('Grafico ventas 2012-2022')
# ax2.grid()
# plt.show()

fig, ax = plt.subplots()

ax.bar(productos, cant_ventas_productos_2024)
ax.set_xlabel('Productos')
ax.set_ylabel('Ventas')
ax.set_title('Grafico ventas 2012-2022')

plt.show()

fig2, ax2 = plt.subplots()

ax2.pie(cant_ventas_productos_2024, labels=productos, autopct='%1.1f%%')
ax2.set_title('Expectativa de ventas 2024')
ax2.grid()
plt.show()