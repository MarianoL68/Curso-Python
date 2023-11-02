#abriendo el archivo con with open
with open("Archivos\\texto_ejemplo.txt") as archivo:

 #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)
    
#no es necesario cerrarlo al usar with open
