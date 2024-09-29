class Pelota():

    def __init__(self, color):
        self.color = color

    @property
    def Color(self):
        return self.color
    
    @Color.setter
    def AsignarColor(self, valor):
        self.color = valor

    def __str__(self) -> str:
        return "AAAAA"
    
    def __add__(self, oo):
        print("Ya no suma")
    

m = Pelota("azul")
print(m)
m.color = "amarilla"
print(m.color)
ma =Pelota("roja")

m+ma

        
m

