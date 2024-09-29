from pizza import Pizza


print(f"Precio: {Pizza.precio}, Tamaño: {Pizza.tamanio}")

if (Pizza.Validar("salsa de tomate",["salsa de tomate", "salsa bbq"])):
    print("Se encuentra")

miPizza = Pizza()
miPizza.RealizarPedido()

print(f"Los ingredientes solicitados son: {miPizza.ingreDienteProteico}, {miPizza.ingredienteVegetal1}, {miPizza.ingredienteVegetal2}")
if (miPizza.esValida):
    print("\033[92m Es una pizza válida. \033[00m")
else:
    print("\033[92m Es una pizza inválida. \033[00m")


#Mostrar error
print(Pizza.esValida)

