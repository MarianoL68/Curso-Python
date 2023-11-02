archivo = open("Archivos\\texto_ejemplo.txt")

#leer archivo completo
#archivo = archivo.read()

#leer una sola linea
#linea = archivo.readline()

#leer linea por linea
lineas = archivo.readlines()

#cerrar el archivo
archivo.close()


print(lineas)
