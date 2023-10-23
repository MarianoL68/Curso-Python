#creando una lista (se pueden modificar)
lista = ["Mariano Loza","Soy Mariano",True,1.82, "Soy Mariano"]

#creando una tupla (no pueden modificar)
tupla = ("Mariano Loza","Soy Mariano",True,1.82, "Soy Mariano")

#esto es vàlido
#lista[3] = "Maquinola"

#esto no
#tupla[3] = "Maquinola"


#creando un conjunto (set) (no se accede a elementos por ìndice, no almacena datos duplicados)
conjunto = {"Mariano Loza","Soy Mariano",True,1.82, "Soy Mariano"}

#print(conjunto[3]) -> no puede acceder al elemento


#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "Mariano Loza",
    'canal' : "Soy Mariano",
    'esta_emocionado' : True,
    'altura' : 1.82,
    'dato_duplicado' : "Soy Mariano"
}

print(diccionario['altura'])