import math

radio = float(input("Ingrese el radio en Kilómetros:"))
g = float(input("Ingrese la constante g:"))

radio = radio*1000
velocidad = math.sqrt(2*radio*g)

print(f"La velocidad de escape es {round(velocidad, 1)} [m/s]")



