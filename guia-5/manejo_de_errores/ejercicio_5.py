def realizar_division():
    archivo = open("guia-5/archivos/texts/divisiones.txt")
    lineas = archivo.readlines()
    archivo.close()
    
    archivo_resultado = open("guia-5/archivos/texts/resultados_divisiones.txt", "w", encoding="utf-8")
    archivo_resultado.write("resultado\n")
    
    for i, linea in enumerate(lineas[1:]):
        try:
            dividendo, divisor = linea.strip().split(";")
            resultado = int(dividendo) / int(divisor)
            archivo_resultado.write(f"{resultado}\n")
        except ValueError:
            archivo_resultado.write(f"Error en la fila {i+2}: Debe ingresar un numero.\n")
        except ZeroDivisionError:
            archivo_resultado.write(f"Error en la fila {i+2}: No se puede dividir por cero.\n")
            
    archivo_resultado.close()

realizar_division()