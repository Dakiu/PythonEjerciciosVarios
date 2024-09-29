class Automovil():
    #Atributos son las variables.
    #Métodos son las funciones.

    puertas = 4

    def __init__(self, marca, modelo, cantidadDeRuedas):
        self.marca = marca
        self.modelo = modelo
        self.cantidadDeRuedas = cantidadDeRuedas
        self.color ="rojo"

    def CualEsMiMarca(self):
        print("La marca es: ", self.marca)

    def CualEsMiMarca(self, fuerte):
        print("La marca es: ", self.marca)

    def CualEsMiMarca(self, fuerte, iio):
        print("La marca es: ", self.marca)
    
    def CuantasRuedasTengo(self):
        print("Tengo ", self.cantidadDeRuedas," ruedas")

    def ColorAutoMovil(self):
        print("El color es ",self.color)

    @staticmethod
    def CuantosVidrios():
        print("Tengo muchos vidrios")

