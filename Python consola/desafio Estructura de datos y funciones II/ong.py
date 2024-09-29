
def factorial(numero):
    acumulador = 1
    while(numero>1):
        acumulador *= numero
        numero -= 1
    return acumulador

def productoria(lista_numeros):
    b = 1
    for a in lista_numeros:
        b *= a
    return b
    
def calcular(**parametros):
    for operacion, valor in parametros.items():
        if operacion.startswith("fact"):       
            resultado = factorial(valor) 
            print("el factorial de", valor, "es", resultado)    
        if operacion.startswith("prod"):
            resultado_2 = productoria (valor)
            print("la productoria de", valor, "es",resultado_2)

calcular(fact_1= 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6 ) 
    