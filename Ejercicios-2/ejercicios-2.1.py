#Falto el profesor y los alumnos van a armar la clase

#Funciom para obtener al profesor y asistente segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    #Creando la lista con los compañeros
    compañeros = []
    
    #Ejecutando un for para pedir información de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: "))
        compañero = (nombre, edad)
        
        #Agregando la informacion a la lista
        compañeros.append(compañero)
        
    #Ordenandolos de mayor a menor según su edad
    compañeros.sort(key=lambda x:x[1])
    
    #Compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre para definir al asiste y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #Retornamos una tupla
    return asistente,profesor

#Desempaquetamos lo que nos retorna la funcion
asistente, profesor = obtener_compañeros(5)

#mostrando el resultado
print(f"El profesor es: {profesor} y su asistente es {asistente}")