from data import df

df['carrera'] = df['carrera'].replace('Informática', 'Informática o Sistemas')

print(df)