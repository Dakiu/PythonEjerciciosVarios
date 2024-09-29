precio_suscripcion = float (input("Ingrese precio \n")) 
numero_usuarios = int (input ("Ingrese numero de usuarios \n"))
gastos_totales = float (input ("Ingrese gastos totales \n"))
utilidades_anterior = float (input ("Ingrese utilidades año anterior \n"))

utilidades_actuales = (precio_suscripcion * numero_usuarios) - gastos_totales
razon = utilidades_actuales/utilidades_anterior

print(f"Razon de Utilidades Actuales y anterior: {razon}")