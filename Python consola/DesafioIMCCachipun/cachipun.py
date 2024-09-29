import random

jugador = ""
volverAJugar = "si"

while volverAJugar=="si":

    while jugador.lower()!="piedra" and jugador.lower()!="papel" and jugador.lower()!="tijera":
        jugador = input("Escribe piedra, papel o tijera: ").lower()

        if jugador!="piedra" and jugador!="papel" and jugador!="tijera":
            print("Argumento inválido: Debe ser piedra, papel o tijera.")

    computadora = random.choice(["piedra", "papel", "tijera"])
    resultado = ""

    if jugador == "piedra" and computadora == "tijera":
        resultado = "¡Ganaste!"
    elif jugador == "papel" and computadora == "piedra":
        resultado = "¡Ganaste!"
    elif jugador == "tijera" and computadora == "papel":
        resultado = "¡Ganaste!"
    elif jugador == computadora:
        resultado = "Empate"
    else :
        resultado = "Perdiste"

    print(" TÚ jugaste:  ", jugador.capitalize())
    print(" Computador jugó: ",computadora.capitalize())
    print (f" {resultado}")

    volverAJugar = input("Si desea volver a Jugar escribir 'Si' ").lower()

    if volverAJugar == "si":
        jugador = ""
