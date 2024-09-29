with open("lorem_ipsum.txt", "r") as file:
    text=file.read()

#primer ejercicio
caracteres = set(text)
print(f"El número de caracteres distintos es: {len(caracteres)}")

#segundo ejercicio
palabras = text.split()
conjunto = set(palabras)
#imprime 241, guía indica 243
print(f"El número de palabras distintas es: {len(conjunto)}")