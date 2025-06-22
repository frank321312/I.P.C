from data import df

df['tiene_mail'] = list(map(lambda x: x != None, df['mail']))

print(df)