class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad 
        
    #Devuelve una representación del objeto en una cadena de texto
    def __str__(self):
        return f"Persona(nombre = {self.nombre},edad = {self.edad})"
    
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)
    
            
mariano = Persona("Mariano",23)
david = Persona("David", 26)
katerina = Persona("Katerina",22)

nueva_persona = mariano + david + katerina
print(nueva_persona)

# repre = repr(mariano)
# resultado = eval(repre)
# print(resultado.nombre)