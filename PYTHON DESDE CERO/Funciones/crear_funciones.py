# #Creando una funcion simple
# def saludar():
#     print("Hola Mariano, ¿Como estás capo?")
    
# #Ejecutando la función simple
# saludar()

#Crrear una función que tenga paramentros
def saludar(nombre, genero):
    genero = genero.lower()
    if(genero == "mujer"):
        adjetivo = "reina"
    elif(genero == "hombre"):
        adjetivo = "rey"
    else: 
        adjetivo = "crack"
        
    print(f"Hola {nombre}, ¿Como estás {adjetivo}?")
    
saludar("sofia", "mujer")
saludar("David", "Hombre")
saludar("andrea", "No-Binario")

#crear una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

#desempaquetando la funciòn
password,primer_numero = crear_contraseña_random(981)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El nùmero utilizado para crearla fue: {primer_numero}") 