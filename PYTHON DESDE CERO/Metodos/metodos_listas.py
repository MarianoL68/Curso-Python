#Creando una lista con list()
lista = list(["hola", "Mariano", 23, True, False, 2000,])

#Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#Agregando un elemento a la lista con append
lista.append("Córdoba")

#Agregando un elemento a la lista en un indice especifico
lista.insert(2, "Loza")

#Agregando varios elementos a la lista
lista.extend([True, 2000])

#Eliminando un elemento de la lista (por su indice)
lista.pop(0) #-1 para eliminar el ultimo, -2 para eliminar el anteultimo, y asi sucesivamente

#Removiendo un elemento de la lista por su valor
lista.remove(True)

#ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(2000)

#eliminando todos los elementos de la lista
lista.clear()

print(elemento_encontrado)