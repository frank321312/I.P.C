from ejercicio_1 import directorio

persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Madrid",
    "email": "ana@example.com",
}

## Escribir una función guardar_diccionario que reciba el diccionario y un nombre de archivo, y guarde el contenido del diccionario en el archivo, en formato CSV, 
## con un par clave-valor por línea.

def guardar_diccionario(diccionario: dict, nombre_archivo, tipo):
    archivo = open(directorio + f"/texts/{nombre_archivo}.{tipo}", "w")
    
    for clave, valor in diccionario.items():
        archivo.write(f"{clave}-{valor}\n")
    
    archivo.close()
    
## guardar_diccionario(persona, "persona_dict")

## Escribir una función cargar_diccionario que reciba el nombre de un archivo con el formato mencionado en el punto anterior, y devuelva el diccionario original.

def cargar_diccionario(nombre_archivo, tipo):
    archivo = open(directorio + f"/texts/{nombre_archivo}.{tipo}", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()
    
    diccionario = {}
    
    for linea in lineas:
        clave, valor = linea.split("-")
        valorStrip = valor.strip()
        diccionario[clave] = int(valorStrip) if valorStrip.isdigit() else valorStrip
        
    return diccionario

print(cargar_diccionario("persona_dict", "csv"))