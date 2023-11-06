#ATRIBUTOS PRIVADOS
# class MiClase:
#     def __init__(self):
#         #la forma de dar a entendet a python que creamos un atributo privado es con el "_" inicial
#         self._atributo_privado = "Valor"
        
#     def _hablar(self):
#         print("Hola")
        
# objeto = MiClase()
# #lo devuelve, se entiende que es un atributo privado, el desalrrolador no debería acceder, pero si quiere lo puede hacer
# print(objeto._atributo_privado)

#ATRIBUTOS MUY PRIVADOS
class MiClase:
    def __init__(self):
        #la forma de dar a entendet a python que creamos un atributo privado es con el "_" inicial
        self.__atributo_privado = "Valor"
        
    def __hablar(self):
        print("Hola")
        
objeto = MiClase()
#lo devuelve, se entiende que es un atributo privado, el desalrrolador no debería acceder, pero si quiere lo puede hacer
# print(objeto._atributo_privado)

#SETTERS Y GETTERS
class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
        
    #getter
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre
    
mariano = Persona("Mariano",21)
nombre = mariano.get_nombre()
print(nombre)

mariano.set_nombre("David")
nombre = mariano.get_nombre()
print(nombre)