#Le pedimos al usuario que nos diga una frase (o varias)
frase = input("Decime una frase y calculo cuanto tardarías si tuvieras que decirla: ")

#Creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#Usamos len() par aver la cantidad de elementos que hay en una lista 
cantidad_de_palabras = len(palabras_separadas)

#En caso de que tarde más de un minuto en decirlo, le decimos que pare
if cantidad_de_palabras > 120:
    print("Tampoco tanto") 

#Calculamos cuanto tardaría en decir las palabras
print(f'Dijiste {cantidad_de_palabras} palabras y tardarías {cantidad_de_palabras/2} segundos en decirlo')
print(f'Yo lo diría en {cantidad_de_palabras * 100 //2 *1.3 / 100} segundos')