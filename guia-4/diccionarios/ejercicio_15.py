## Los estudiantes de la materia Pensamiento Computacional quieren crear un programa que les facilite la cursada. Uno de los problemas es que no se tiene fácil acceso a los 
## enunciados de los ejercicios, porque la guía es larga y hay que scrollear mucho. En el programa, la guía de ejercicios se guarda en un diccionario, donde cada clave es el número 
## de guía y cada valor una lista con los enunciados de los ejercicios, cada uno en su posición correspondiente (la posición 0 de la lista sólo guarda None). 
## Se quiere que el usuario que está usando el programa pueda acceder por pantalla a un enunciado puntual de una guía con sólo pedirlo (si existe). 
## Para el problema mencionado, hacer una función o más que lo resuelva.

guias = {
    1: [None, "Enunciado ejercicio 1", "Enunciado ejercicio 2", "Enunciado ejercicio 3"],
    2: [None, "Enunciado ejercicio 1", "Enunciado ejercicio 2"],
    3: [None, "Enunciado ejercicio 1", "Enunciado ejercicio 2", "Enunciado ejercicio 3", "Enunciado ejercicio 4"]
}

def obtener_enunciado(guia, num_enunciado, guias: dict = guias):
    if (guia not in guias):
        print("Guia no encontrada")
        return
    
    if (num_enunciado > len(guias[guia]) or num_enunciado < 1):
        print(f"Guia {guia}, enunciado {num_enunciado} no encontrado")
        return
    
    print(guias[guia][num_enunciado])

obtener_enunciado(2, 2)