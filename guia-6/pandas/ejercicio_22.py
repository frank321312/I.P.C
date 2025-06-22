from data import df

df['edad'] = [21, 23, 25, 27, 29, 22, 30]

df = df.sort_values(by=['carrera', 'edad'], ascending=[True, False])

print(df)