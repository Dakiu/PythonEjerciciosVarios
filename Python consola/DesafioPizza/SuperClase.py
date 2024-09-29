class SuperClase():

    def __init__(self):
        self.__uno = 1
        self.dos = 2
    
    def Saltar(self):
        self.tres=3

    @property
    def Uno(self):
        return self.__uno
    
    @Uno.setter
    def AsignarUno(self, valor):
        self.__uno=valor
     
class ClaseBaja(SuperClase):


    def Correr(self):
        self.__cuatro =4
    
    @property
    def cuatro(self):
        return self.__cuatro
    
    @cuatro.setter
    def cuatro(self, valor):
        self.__cuatro=valor




sc = SuperClase()
print(sc.dos)

sdd = ClaseBaja()
sdd.Correr()
print(sdd.cuatro)
