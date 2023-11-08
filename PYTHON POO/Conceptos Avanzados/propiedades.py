class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre
        
    @nombre.deleter
    def nombre(self):
        del self.__nombre
    
    
mariano = Persona("Mariano",21)
nombre = mariano.nombre

print(nombre)

mariano.nombre = "David"

del mariano.nombre
