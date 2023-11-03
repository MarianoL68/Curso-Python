class Persona: 
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad 
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print(f"Hola soy {self.nombre}, te estoy hablando")
        

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
                
          
class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
       print (f"Hola, soy, {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}")
    
    
jose = EmpleadoArtista("Jose",38,"argentino","cantar",300000,"Ford")

herencia = issubclass(EmpleadoArtista,Artista)
instancia = isinstance(jose,Artista)

print(instancia)

