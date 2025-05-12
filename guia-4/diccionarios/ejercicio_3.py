## a.Se deberá simular una persona que tira un dado N veces, y se deberá devolver un diccionario con la cantidad de apariciones de cada 
## valor en el dado. Nota: para simular una tirada, usar import randomy random.randint(1, 6).

from random import randint

def tirar_dado_n_veces(n: int):
    diccionario = {}
    for _ in range(n):
        valor_dado = randint(1, 6)

        if (str(valor_dado) in diccionario):
            diccionario[str(valor_dado)] += 1
        else:
            diccionario[str(valor_dado)] = 1

    return diccionario

print(tirar_dado_n_veces(10))

## b.Repetir el punto anterior, si ahora en vez de tirar 1 dado, tira 2. Se debe devolver un diccionario con la cantidad de apariciones de cada valor de la suma de ambos dados.

def tirar_dos_dados_n_veces(n: int):
    diccionario = {}

    for _ in range(n):
        valor_dado1 = randint(1, 6)
        valor_dado2 = randint(1, 6)

        for i in [valor_dado1, valor_dado2]:
            if (str(i) in diccionario):
                diccionario[str(i)] += 1
            else:
                diccionario[str(i)] = 1

    return diccionario

print(tirar_dos_dados_n_veces(10))