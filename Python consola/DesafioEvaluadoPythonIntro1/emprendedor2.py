# Utilidades = p * u - gtd
# utilidades = ((p * u) + 1.5 * precio_suscripcion * usuarios_premium) - gastos_totales
precio_suscripcion = float (input("Ingrese precio: \n")) 
usuarios_normales = int (input ("Ingrese numero de usuarios: \n"))
usuarios_premium = int (input ("Ingrese numeros de usuarios premium: \n"))
gastos_totales = float (input ("Ingrese gastos totales: \n") ) 

utilidades = ((precio_suscripcion * usuarios_normales) + 1.5 * precio_suscripcion * usuarios_premium) - gastos_totales
print (f"Las Utilidades son: {utilidades}")