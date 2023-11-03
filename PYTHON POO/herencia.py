class Persona: 
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad 
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print(f"Hola soy {self.nombre}, te estoy hablando")
        
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
    #Puedo sobreescribir el metodo.
    def hablar(self):
        print(f"Hola soy {self.nombre} y trabajo de {self.trabajo}")
        
carlos = Empleado("Carlos",50,"argentino","panadero","150000")

carlos.hablar()

