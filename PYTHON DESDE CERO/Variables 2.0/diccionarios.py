#creando diccionarios con dict()
diccionario = dict(nombre="Mariano",apellido="Loza")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Belgrano","Celeste" ]):"Córdoba"}

#creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"No se")

print(diccionario["nombre"])

