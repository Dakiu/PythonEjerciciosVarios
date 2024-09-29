respuesta = ""
si="si"
no="no"

while respuesta.lower()!=si and respuesta.lower()!=no:
    respuesta = input(" ¿Responde a estímulos? Ingrese 'Si' o 'No' \n").lower()
    respuesta = respuesta.replace('í','i')

    if respuesta!=si and respuesta!=no:
        print("Respuesta incorrecta, debe ser 'Si' o 'No'.\n")
    elif respuesta == si:
        print("Valorar la necesidad de llevarlo al hospital más cercano.\n")
        break
    elif respuesta == no:
        print("Abrir la vía aérea")
        respuesta = ""
        while respuesta.lower()!=si and respuesta.lower()!=no:
            respuesta = input("¿Respira? Ingrese 'Si' o 'No'\n").lower()
            respuesta = respuesta.replace('í','i')
            if respuesta!=si and respuesta!=no:
                print("Respuesta incorrecta, debe ser 'Si' o 'No'.\n")
            elif respuesta == si:
                print("Permitirle posición de suficiente ventilación\n")
                break
            elif respuesta == no:
                print("Administrar 5 ventilaciones y llamar a la ambulancia")
                llegoAmbulancia=no
                respuesta = ""
                while respuesta.lower()!=si and respuesta.lower()!=no:
                    while llegoAmbulancia==no:
                        respuesta = input("¿Signos de vida? Ingrese 'Si' o 'No'\n").lower()
                        respuesta = respuesta.replace('í','i')
                        if respuesta!=si and respuesta!=no:
                            print("Respuesta incorrecta, debe ser 'Si' o 'No'.\n")
                        elif respuesta == si:
                            print("Reevaluar a la espera de la ambulancia")
                        elif respuesta==no:
                            print("Administrar comprensiones torácicas hasta que llegue la ambulancia,")
                        respuesta = input("¿Llegó la ambulancia? Ingrese Si o No\n")
                        llegoAmbulancia = respuesta
                        if llegoAmbulancia==si:
                            break



                    
                
        
        
    
