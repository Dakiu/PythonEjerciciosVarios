from string import ascii_lowercase
from getpass import getpass

password = getpass("Ingrese la contraseña oculta: ")

letrasCorrecta = 0
intentos = 0

for l in password:
    for letra in ascii_lowercase:
        intentos +=1
        if letra==l:
            letrasCorrecta +=1
            break


if letrasCorrecta == len(password):
    print(" La contraseña fue forzada en ",intentos, " intentos. ")

