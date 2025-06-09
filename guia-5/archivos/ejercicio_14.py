from ejercicio_1 import directorio

def sala_pelicula(archivo_sala, archivo_pelicula):
    leer_sala = open(directorio + f"/texts/{archivo_sala}.txt")
    lineas_sala = leer_sala.readlines()
    leer_sala.close()
    leer_pelicula = open(directorio + f"/texts/{archivo_pelicula}.txt")
    lineas_pelicula = leer_pelicula.readlines()
    leer_pelicula.close()
    crear_sala_pelicula = open(directorio + f"/texts/funciones.csv", "w")    
    
    for i in range(len(lineas_pelicula)):
        crear_sala_pelicula.write(f"{lineas_sala[i].strip()};{lineas_pelicula[i]}")
    
    crear_sala_pelicula.close()
    print("Archivo creado exitosamente.")

sala_pelicula("salas", "peliculas")