with open('Archivos\\texto_ejemplo.txt','a') as archivo:
    #usando un bucle para agregar varias lineas
    archivo.write("\n")
    for i in range(5):
        #agregando lineas
        archivo.write(f"Linea {i+1} agregada\n")