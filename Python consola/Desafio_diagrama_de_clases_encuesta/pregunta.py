# Requerimiento 3.1. Importar la clase Alternativa, y crear la clase Pregunta
from alternativa import Alternativa

class Pregunta:
    """
    Clase que representa una pregunta en una encuesta.

    Atributos:
        enunciado (str): El enunciado de la pregunta.
        ayuda (str): Información opcional adicional sobre la pregunta.
        alternativas (list): Lista de alternativas para la pregunta.
        requerido (bool): Indica si la pregunta es obligatoria.
    """

    # Requerimiento 3.2. Definir constructor que recibe los valores para los atributos de instancia enunciado,
    # ayuda, alternativas y requerido
    def __init__(self, enunciado: str, ayuda: str, alternativas: list, requerido: bool) -> None:
        """
        Inicializa una instancia de la clase Pregunta.

        Args:
            enunciado (str): El enunciado de la pregunta.
            ayuda (str, opcional): Información adicional sobre la pregunta.
            alternativas (list): Lista de diccionarios con alternativas.
            requerido (bool): Indica si la pregunta es obligatoria.
        """
        # Pseudocódigo:
        # Establecer el enunciado de la pregunta
        # Establecer la ayuda de la pregunta (opcional)
        # Crear una lista de instancias de la clase Alternativa a partir de la lista de alternativas
        # Establecer si la pregunta es obligatoria
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.__alternativas = [Alternativa(a["contenido"], a["ayuda"]) for a in alternativas]
        self.requerido = requerido

    # Requerimiento 3.3. A continuación, se define el método mostrar_pregunta (se agrega implementación)
    def mostrar_pregunta(self) -> None:
        """
        Muestra el enunciado de la pregunta, su ayuda y sus alternativas.
        """
        # Pseudocódigo:
        # Imprimir el enunciado de la pregunta
        # Si hay ayuda disponible, imprimir la ayuda

        # Para cada alternativa en la lista de alternativas, llamar al método mostrar_alternativa

        # Tip: if_

        # Tip: ciclo for
