from data import df

df = df.sort_values(by=['carrera', 'apellido'], ascending=[True, True])

print(df)