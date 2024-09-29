class Error(Exception):
    pass

class LargoExcedidoException(Error):

    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje

    def __str__(self) -> str:
        print("Largo Excedido")

class SubTipoInvalidoException(Error):

    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        print("subtipo inválido")