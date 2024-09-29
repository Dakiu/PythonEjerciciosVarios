precio_suscripcion = float (input("Ingrese Precio\n ")) 
numero_usuarios = int (input ("Ingrese numero de usuarios \n"))
gastos_totales = float (input ("Ingrese gastos totales\n ") )
utilidades = (precio_suscripcion * numero_usuarios) - gastos_totales
print ( f"Las Utilidades son: {utilidades}" )