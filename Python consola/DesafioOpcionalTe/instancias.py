# Paso 4: Importar la clase Te
from te import Te

# Crear dos instancias de la clase Te
# ingresa tu código acá
teNegro = Te(1, "300", "3", "desayuno")
teVerde = Te(2, "300", "5", "mediodia")


# Almacenar el tipo de dato de cada instancia
# ingresa tu código acá
tipoTeNegro = type(teNegro)
tipoTeVerde = type(teVerde)
# Mostrar por pantalla el valor de cada tipo de dato
# ingresa tu código acá
print(tipoTeVerde)
print(tipoTeNegro)

# Verificar si ambos tipos son iguales y mostrar el mensaje correspondiente
# ingresa tu código acá

if (tipoTeNegro == tipoTeVerde):
    print("Ambos objetos son del mismo tipo”")
else:
    print("Los objetos no son del mismo tipo")

"""
 duracion = 365
    sabores=""#negro verde infusion
    formato=""#300gr ($3000) 500gr($5000)
    preparacion=0 #te negro preparacion 3 minutos(desayuno), verde 5 minutos(mediodia), aguaHierbas 6 minutos(atardecer)
"""