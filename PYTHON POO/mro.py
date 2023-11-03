class A:
    def hablar(self):
        print("Hola desde A")
        
class F:
    def hablar(self):
        print("Hola desde F")
        
class B(A):
    def hablar(self):
        print("Hola desde A")
        
class C(F):
    def hablar(self):
        print("Hola desde A")
        
class D(B,C):
    def hablar(self):
        print("Hola desde A")
        
d = D()

d.hablar()

print(D.mro())