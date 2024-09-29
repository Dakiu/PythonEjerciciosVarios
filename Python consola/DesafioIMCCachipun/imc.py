peso = float(input("Ingrese el peso en kilos: \n "))
altura = float(input("Ingrese la altura en centímetros: \n ")) /100
IMC = peso / altura ** 2

categoria = ""

if IMC < 18.5:
    categoria = "bajo peso"
elif IMC >= 18.5 and IMC < 25:
    categoria = "Adecuado"
elif IMC >= 25 and IMC < 30:
    categoria = "Sobrepeso"
elif IMC >= 30 and IMC < 35:
    categoria = "Obesidad  Grado I"
elif IMC >=35 and IMC <40:
    categoria = "Obesidad Grado II"
elif IMC > 40:
    categoria = "Obesidad Grado III" 

   
    
print ("su IMC es:\n  ", round (IMC, 2))
print ("La clasificación OMS es: ", categoria )