from data import df

df['edad'] = [21, 23, 25, 27, 29, 22, 30]

print(df[df['edad'] > 25])