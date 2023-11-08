class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    #Metodos
    def llamar(self):
        print(f'Estas haciendo un llamado desde un: {self.modelo}')
        
    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')
    
celular1 = Celular("Apple","Iphone 14","48MP")
celular2 = Celular("Samsung","S23","96MP")

celular2.cortar()