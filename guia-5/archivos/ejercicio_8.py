## Se tiene un archivo con una pregunta, llamado pregunta.txt. Se pide leerlo y mostrar el contenido en consola. 
## Luego, pedirle al usuario una respuesta, y guardarla en un archivo llamado respuesta.txt.

from ejercicio_1 import directorio

def responder_pregunta(nombre_pregunta, tipo_pregunta, nombre_respuesta, tipo_respuesta):
    archivo_pregunta = open(directorio + f"/texts/{nombre_pregunta}.{tipo_pregunta}", encoding="utf-8")
    linea = archivo_pregunta.readline().strip()
    archivo_pregunta.close()
    
    print(linea)
    
    respuesta = input("Respuesta: ")
    
    archivo_respuesta = open(directorio + f"/texts/{nombre_respuesta}.{tipo_respuesta}", "w")
    archivo_respuesta.write(respuesta)
    archivo_respuesta.close()
    
responder_pregunta("pregunta", "txt", "respuesta", "txt")