import ingredientes

class Pizza:

    precio = 10000
    tamanio = "familiar"

    @staticmethod
    def Validar(elemento, lista):
    
        if elemento not in lista:
            return False
        else:
            return True
    
    def RealizarPedido(self):

        ingreDienteProteico =input(f"Ingresar Ingrediente Proteico (\033[94m {ingredientes.proteicos} \033[00m \n")
        ingredienteVegetal1 = input(f"Ingresar primer ingrediente vegetal (\033[91m {ingredientes.vegetales} \033[00m \n")
        ingredienteVegetal2 = input(f"Ingresar segundo ingrediente vegetal  (\033[91m {ingredientes.vegetales} \033[00m \n")
        tipoMasa = input(f"Ingresar tipo de Masa  (\033[95m {ingredientes.masa} \033[00m \n")

        self.ingreDienteProteico = ingreDienteProteico
        self.ingredienteVegetal1 = ingredienteVegetal1
        self.ingredienteVegetal2 = ingredienteVegetal2
        self.tipoMasa = tipoMasa

        self.esValida = False
        if (self.Validar(ingreDienteProteico, ingredientes.proteicos) 
            and self.Validar(ingredienteVegetal1,ingredientes.vegetales)
            and self.Validar(ingredienteVegetal2, ingredientes.vegetales)
            and self.Validar(tipoMasa, ingredientes.masa)):
            self.esValida = True



