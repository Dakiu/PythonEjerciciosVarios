
from te import Te

sabor = input("Ingresar sabor (1) Te Negro (2) Te Verde (3)Agua Hierba\n")

formato = int(input("Ingresar formato (300) o (500)\n"))

tiempo,recomendacion =Te.retorna_tiempo_y_recomendacion(sabor)

precio =Te.retorna_precio(formato)

if sabor==1:
    sabor="Te Negro"
elif sabor==2:
    sabor="Te Verde"
else:
    sabor="Agua Hierba"

print(f"Sabor {sabor}, Formato {formato}, precio {precio}, Tiempo {tiempo} recomendación {recomendacion}")
