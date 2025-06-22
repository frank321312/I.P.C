from data import df

df['pedir_mail'] = list(map(lambda x: x == None, df['mail']))

print(df)