## Escribir una función para determinar si una letra recibida es vocal o no. La misma debe devolver un valor booleano. Luego, escribir una función para determinar si una letra es consonante o no.

## a.Resolver sin el uso de in ni not in.
## b.Resolver usando in y not in.
## c.Resolver para que la función identifique tanto mayúsculas como minúsculas.

def es_vocal_sin_in_ni_not_in(char):
    char_m = str.lower(char) 
    return char_m == "a" or char_m == "e" or char_m == "i" or char_m == "o" or char_m == "u"

def es_consonante_sin_in_ni_not_in(char):
    char_m = str.lower(char) 
    return char_m == 'b' or char_m == 'c' or char_m == 'd' or char_m == 'f' or char_m == 'g' or char_m == 'h' or char_m == 'j' or char_m == 'k' or char_m == 'l' or char_m == 'm' or char_m == 'n' or char_m == 'p' or char_m == 'q' or char_m == 'r' or char_m == 's' or char_m == 't' or char_m == 'v' or char_m == 'w' or char_m == 'x' or char_m == 'y' or char_m == 'z'

def es_vocal_con_in(char):
    return str.lower(char) in "aeiou"

def es_consonante_con_in(char):
    return str.lower(char) in "bcdfghjklmnpqrstvwxyz"

def es_vocal_con_not_in(char):
    return str.lower(char) not in "bcdfghjklmnpqrstvwxyz"

def es_consonante_con_not_in(char):
    return str.lower(char) not in "aeiou"

print(es_vocal_sin_in_ni_not_in("A"))
print(es_consonante_sin_in_ni_not_in("b"))
print(es_consonante_con_in("i"))
print(es_consonante_con_in("e"))
print(es_vocal_con_not_in("b"))
print(es_consonante_con_not_in("p"))