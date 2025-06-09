def filtrar_temperaturas(nombre_archivo):
    archivo = open(f"guia-5/archivos/texts/{nombre_archivo}", "r")
    lineas = archivo.readlines()
    archivo.close()
    
    temperaturas_validas = []
    
    for linea in lineas:
        try:
            temperatura = float(linea.strip())
            temperaturas_validas.append(temperatura)
        except ValueError:
            continue
    
    promedio = sum(temperaturas_validas) / len(temperaturas_validas) if temperaturas_validas else 0
    porcentaje_ignorados = (len(lineas) - len(temperaturas_validas)) / len(lineas) * 100 if lineas else 0
    return round(promedio, 2), round(porcentaje_ignorados, 2)

temperaturas = filtrar_temperaturas("temperaturas.txt")
print("Promedio:", temperaturas[0])
print("Porcentaje de valores ignorados:", temperaturas[1], "%")