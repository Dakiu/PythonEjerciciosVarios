# Requerimiento 2.1. Crear la clase Alternativa, con su constructor, el cual recibe los valores para asignar a
# los atributos de instancia contenido y ayuda.

class Alternativa:
    """
    Clase que representa una alternativa en una pregunta de una encuesta.

    Atributos:
        contenido (str): El contenido de la alternativa.
        ayuda (str): Información opcional adicional sobre la alternativa.
    """

    def __init__(self, contenido: str, ayuda: str = None) -> None:
        """
        Inicializa una instancia de la clase Alternativa.

        Args:
            contenido (str): El contenido de la alternativa.
            ayuda (str, opcional): Información adicional sobre la alternativa.
        """
        # Pseudocódigo:
        # Establecer el contenido de la alternativa
        # Establecer la ayuda de la alternativa (opcional)


    # Requerimiento 2.2. En la misma clase, agregar el método mostrar_alternativa (se agregó implementación)
    def mostrar_alternativa(self) -> None:
        """
        Muestra el contenido de la alternativa y su ayuda si está disponible.
        """
        # Pseudocódigo:
        # Imprimir el contenido de la alternativa
        # Si hay ayuda disponible, imprimir la ayuda
        # Tip: if

