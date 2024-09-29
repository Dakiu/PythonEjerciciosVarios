import sys
precios = {'Notebook': 700000,
 'Teclado': 25000,
 'Mouse': 12000,
 'Monitor': 250000,
 'Escritorio': 135000,
 'Tarjeta de Video': 1500000}

operacion= "mayor"
umbral = int(sys.argv[1])
if len(sys.argv)>2:
    operacion = (sys.argv[2])

if operacion == "mayor":
    productos={equipo for equipo, valor in precios.items() if valor >umbral}
    print ("Los productos mayores al umbral son:",', '.join(productos))  
elif operacion == "menor":
   productos={equipo for equipo, valor in precios.items() if valor < umbral}
   print ("Los productos menor al umbral son:",', '.join(productos))  
else:
    print("Lo sentimos, no es una operación válida")









