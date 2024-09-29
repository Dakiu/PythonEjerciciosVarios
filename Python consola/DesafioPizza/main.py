from auto import Automovil


moto = Automovil("marcaMoto","modeloMoto",4) #instanciar

moto.CualEsMiMarca(5)
moto.CuantasRuedasTengo()
moto.ColorAutoMovil()

triciclo = Automovil("marcaTriciclo","modeloTriciclo",2)
triciclo.CualEsMiMarca(5)
triciclo.CuantasRuedasTengo()
triciclo.ColorAutoMovil()

auto = Automovil("marcaAuto222","modeloAuto",6)
auto.CualEsMiMarca(5)
auto.CuantasRuedasTengo()
auto.ColorAutoMovil()

print("Marca Auto", auto.marca)

Automovil.CuantosVidrios()
print(auto.puertas)
print(triciclo.puertas)



