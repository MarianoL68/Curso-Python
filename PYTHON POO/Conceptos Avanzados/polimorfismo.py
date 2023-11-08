class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "Guau"
    

def hacer_sonido(animal):
    print(animal.sonido())
    
gato = Gato()
perro = Perro ()

hacer_sonido(perro)

print(gato.sonido())

#Polimorfismo de cohersion
num1 = 3
num2 = 4.4

resultado = num1 + num2

print(resultado)
print(type(resultado))