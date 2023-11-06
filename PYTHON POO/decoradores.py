def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
    return funcion_modificada

# def saludo():
#     print("Hola, que onda?")
    
# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    print("Hola, que onda?")
    
saludo()