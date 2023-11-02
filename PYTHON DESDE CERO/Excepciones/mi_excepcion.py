#creando mi propia excepción personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"cometiste el siguiente error: {err}")
        

#Lanzando mi propia excepcion
#raise MiExcepcion("Jajajajaja, persona poco culta")

#manejandola
try:
    raise MiExcepcion("tremendo error")
except:
    print("Como vas a cometer ese error?")