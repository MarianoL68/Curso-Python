with open("Archivos\\texto_ejemplo.txt","w") as archivo:
    # #sobreescricribiendo el archivo
    # archivo.write("Reescribiendo el archivo")
    
    #agregando 2 lineas con writelines
    archivo.writelines([" - Hola maestro como andas\n"," - misericordia\n"])
    
    #agregando otras 2 lineas
    archivo.writelines([" - no se porque dijiste eso\n"," - yo tampoco"])