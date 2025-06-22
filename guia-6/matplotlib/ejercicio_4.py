from polars import df
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

## Punto A
# order = df.sort_values(by=['Población (hab)'], ascending=[True])

# ax.barh(order['Jurisdicción'], order['Población (hab)'])
# ax.set_xlabel("Jurisdicción")
# ax.set_ylabel('Población (hab)')
# ax.set_title('Cantidad de habitantes por jurisdicción')

# plt.show()

## Punto B
# ax.pie(df['Superficie (km2)'], labels=df['Jurisdicción'], autopct='%1.1f%%')
# ax.set_title('Porcentaje de superficie de cada región')
# plt.show()

## Punto C
# order_pbi = df.sort_values(by=['PBI'], ascending=[True])

# ax.bar(order_pbi['Jurisdicción'], order_pbi['PBI'])
# ax.set_xlabel("Jurisdicción")
# ax.set_ylabel('PBI')
# ax.set_title('PBI de cada jurisdicción')

# plt.show()

## Punto D
## El grafico no es del todo exacto, ubica jurisdicciones por debajo del medio millon siendo B.A la excepcion
# ax.scatter(df['Población (hab)'], df['Superficie (km2)'])
# ax.grid()

# plt.show()