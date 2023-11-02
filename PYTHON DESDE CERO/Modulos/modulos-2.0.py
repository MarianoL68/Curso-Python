#si el modulo estuviera dentro de una carpeta en la misma ruta 
# import Funciones_Buenas.saludar as m_saludar

import sys

sys.path.append('C:\\Curso-Python-SD\\Funciones_Buenas')

import saludar as modulo_saludo

print(modulo_saludo.saludar("Mariano"))