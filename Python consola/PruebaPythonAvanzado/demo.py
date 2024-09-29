from campana import Campana
from datetime import date, datetime
from error import LargoExcedidoException, SubTipoInvalidoException


c = Campana("Campaña Demo", date.today(), date.today(), 
    [{"tipo": "video", "url_clic": "sin-url", "url_archivo": "sin-url", "sub_tipo": "instream", "duracion": 30}])
# c = Campana("Campaña Demo", date.today(), date.today(), 
#     [{"tipo": "video", "url_clic": "sin-url", "url_archivo": "sin-url", "sub_tipo": "instream", "duracion": 30},
#      {"tipo": "display","ancho":100, "alto":100, "url_clic": "sin-url", "url_archivo": "sin-url", "sub_tipo": "tradicional"}
# ])


try:
    c.nombre = input("Ingrese nombre de la campaña:\n")
    c.anuncios[0].sub_tipo=input("Ingrese subtipo de la campaña:\n")
    print(c)
except LargoExcedidoException as largoException:
    print("Largo Excedido en nombre de Campaña.")
    with open("error.log", "a+") as log:
        now = datetime.now()
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {largoException.__class__.__name__} ERROR:{largoException.mensaje}\n")
except SubTipoInvalidoException as subTipoInvalido:
      print("Sub Tipo Inválido.")
      with open("error.log", "a+") as log:
        now = datetime.now()
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {subTipoInvalido.__class__.__name__} ERROR:{subTipoInvalido.mensaje}\n")


