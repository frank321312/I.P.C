def procesar_lineas(ruta, archivos):
    reporte_lineas = open(f"guia-5/archivos/texts/reporte.csv", "w")
    reporte_lineas.write("ruta;archivo;cant_linea\n")
    
    for nombre in archivos:
        abrir_archivo = open(f"{ruta}/{nombre}", "r", encoding="utf-8")
        lineas = abrir_archivo.readlines()
        abrir_archivo.close()
        filtrar_codigo = list(filter(lambda x: x.count("#") == 0 and x.count("def") == 0 and x != "\n", lineas))
        if (len(filtrar_codigo) > 5):
            reporte_lineas.write(f"{ruta};{nombre};{len(filtrar_codigo)}\n")
        
    reporte_lineas.close()

procesar_lineas("guia-2", [f"ejercicio_{i+1}.py" for i in range(20)])