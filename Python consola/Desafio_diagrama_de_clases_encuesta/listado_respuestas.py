# Requerimiento 6.1. Importar la clase Usuario, y definir la clase ListadoRespuestas con su constructor, el
# cual define los atributos de instancia del diagrama.
from usuario import Usuario

class ListadoRespuestas:
    """
    Clase que representa un listado de respuestas de un usuario a una encuesta.

    Atributos:
        usuario (Usuario): El usuario que generó el listado de respuestas.
        respuestas (list): Lista de respuestas del usuario.
    """

    def __init__(self, usuario: Usuario, respuestas: list) -> None:
        """
        Inicializa una instancia de la clase ListadoRespuestas.

        Args:
            usuario (Usuario): El usuario que generó el listado de respuestas.
            respuestas (list): Lista de respuestas del usuario.
        """
        # Pseudocódigo:
        # Establecer el usuario que generó el listado de respuestas
        # Establecer la lista de respuestas del usuario


    # Requerimiento 6.2. Se agrega propiedades para leer atributos.
    @property
    def usuario(self) -> Usuario:
        """
        Devuelve el usuario que generó el listado de respuestas.

        Returns:
            Usuario: El usuario que generó el listado de respuestas.
        """
        # Pseudocódigo:
        # Retornar el usuario que generó el listado de respuestas


    @property
    def respuestas(self) -> list:
        """
        Devuelve la lista de respuestas del usuario.

        Returns:
            list: Lista de respuestas del usuario.
        """
        # Pseudocódigo:
        # Retornar la lista de respuestas del usuario

