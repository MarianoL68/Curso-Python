#DEPENDENCY INVERSION PRINCIPLE

# #Esto esta mal porque CorrectorOrtografico esta dependiendo de 
# # Dicciionario, si algo cambia en Diccionario tambien hay que 
# # cambiarlo en Corrector ortografico  
# class Diccionario:
#     def verificar_palabra(self,palabra):
#         #Logico para verificar palabras
#         pass
    
# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self,texto):
#         #Usamos el diccionario para corregir el texto
#         pass

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Lógica para verificar palabras en el diccionario
        pass
    
class CorrectorOrtografico:
    def __init__(self,verificador):
        self.verificar = verificador
        
    def corregir_texto(self,texto):
        #Usamos el verificador para corregir texto
        pass
    
    