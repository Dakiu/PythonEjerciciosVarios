from usuario import Usuario
import json
from datetime import datetime

instancia = []

with open("usuarios.txt", "r") as usuarios:
    linea = usuarios.readline()
    while linea:
        try: 
            usuario = json.loads(linea)
            instancia.append(Usuario(usuario.get("nombre"), usuario.get("apellido"), usuario.get("email"), usuario.get("genero")))
        except Exception as e:
            with open("error.log", "a+") as log:
                now = datetime.now()
                log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR:{e}\n")
        finally:
            linea = usuarios.readline()