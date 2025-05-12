## a.Inserte el caracter entre cada letra de la cadena.

def insertar_caracter_por_cada_letra(cadena: str, caracter: str, cantidad):
    nueva_cadena = cadena.replace("", caracter, cantidad)
    return nueva_cadena[0 if cantidad == 0 else 1 :len(nueva_cadena)-1]

print(insertar_caracter_por_cada_letra("separar", "-", 0))

## b.Reemplace todos los espacios por el caracter. 

def reemplazar_caracter_por(cadena: str, caracter: str, cantidad):
    return cadena.replace(" ", caracter, cantidad)

print(reemplazar_caracter_por("mi archivo de texto.txt", "_", 0))

## c.Reemplace todos los dígitos de la cadena por el caracter.

def reemplazar_digito_por(cadena: str, caracter: str, cantidad):
    nueva_cadena = ""
    contador = 0

    if (cantidad == 0):
        return cadena

    for i in range(len(cadena)):
        if (cadena[i].isdigit()):
            nueva_cadena += caracter
            contador += 1
            if (contador == cantidad):
                nueva_cadena += cadena[i+1::]
                break
        else: 
            nueva_cadena += cadena[i]
    
    return nueva_cadena

print(reemplazar_digito_por("su clave es: 1540", "*", 0))

## d.Inserte el caracter cada 3 dígitos en la cadena. 

def insertar_cada_3_digitos_un_caracter(cadena: str, caracter: str, cantidad):
    nueva_cadena = ""
    contador = 0
    contador_cantidad = 0

    if (cantidad == 0): 
        return cadena

    for i in range(len(cadena)):
        if (contador == 3):
            nueva_cadena += caracter
            nueva_cadena += cadena[i]
            contador = 0
            contador_cantidad += 1
            if (contador_cantidad == cantidad):
                nueva_cadena += cadena[i+1::]
                break
        else:
            nueva_cadena += cadena[i]

        contador += 1

    return nueva_cadena

print(insertar_cada_3_digitos_un_caracter("12381273892178421", ".", 0))

## Modificar todas las anteriores para que, adicionalmente, reciba un parámetro que indique la cantidad máxima de reemplazos o inserciones a realizar.