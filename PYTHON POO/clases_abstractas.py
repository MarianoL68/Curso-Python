from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,genero,actividad):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,genero,actividad):
        super().__init__(nombre,edad,genero,actividad)
        
    def hacer_actividad(self):
        print(f"Estoy estudiando {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self,nombre,edad,genero,actividad):
        super().__init__(nombre,edad,genero,actividad)
        
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en {self.actividad}")

mariano = Estudiante("Mariano",23,"masculino","programacion")
jorge = Trabajador("Catalina",35,"femenino","programación")

mariano.presentarse()
mariano.hacer_actividad()
jorge.presentarse()
jorge.hacer_actividad()