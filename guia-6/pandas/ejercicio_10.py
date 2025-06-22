from data import df

persona = df.iloc[[round(df.shape[0] / 2) - 1]]

print(persona)