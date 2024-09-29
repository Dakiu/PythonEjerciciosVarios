
sol_peruano = float(input("Ingrese el valor del sol peruano "))
peso_argentino = float(input("Ingrese el valor del peso argentino "))
dolar_americano = float(input("Ingrese el valor del dolar americano "))
peso_chileno = float(input("Ingrese el valor del peso chileno "))


sol_peruano *= peso_chileno 
peso_argentino *= peso_chileno
dolar_americano *= peso_chileno

print(f"Los {peso_chileno} pesos equivalen a \n {sol_peruano} Soles\n {peso_argentino} Pesos Argentinos\n {dolar_americano} Dólares\n")
      
        
