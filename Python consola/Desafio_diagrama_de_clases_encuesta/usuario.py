# Requerimiento 5.1. Importar las clases Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion,
# ListadoRespuestas (dará error hasta que se defina), y Union del módulo typing.
from typing import Union
from encuesta import Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion
from listado_respuestas import ListadoRespuestas

class Usuario:
    """
    Clase que representa un usuario.

    Atributos:
        correo (str): El correo electrónico del usuario.
        edad (int): La edad del usuario.
        region (int): La región del usuario.
    """

    # Requerimiento 5.2. Definir el constructor con los atributos del diagrama
    def __init__(self, correo: str, edad: int, region: int) -> None:
        """
        Inicializa una instancia de la clase Usuario.

        Args:
            correo (str): El correo electrónico del usuario.
            edad (int): La edad del usuario.
            region (int): La región del usuario.
        """
        # Pseudocódigo:
        # Establecer el correo electrónico del usuario
        # Establecer la edad del usuario
        # Establecer la región del usuario


    # Requerimiento 5.3. Agregar propiedades con sus métodos
    @property
    def correo(self) -> str:
        """
        Devuelve el correo electrónico del usuario.

        Returns:
            str: El correo electrónico del usuario.
        """
        # Pseudocódigo:
        # Retornar el correo electrónico del usuario


    @correo.setter
    def correo(self, correo) -> None:
        """
        Establece el correo electrónico del usuario.

        Args:
            correo (str): El correo electrónico del usuario.
        """
        # Pseudocódigo:
        # Establecer el correo electrónico del usuario


    @property
    def edad(self) -> int:
        """
        Devuelve la edad del usuario.

        Returns:
            int: La edad del usuario.
        """
        # Pseudocódigo:
        # Retornar la edad del usuario


    @edad.setter
    def edad(self, edad) -> None:
        """
        Establece la edad del usuario.

        Args:
            edad (int): La edad del usuario.
        """
        # Pseudocódigo:
        # Establecer la edad del usuario


    @property
    def region(self) -> int:
        """
        Devuelve la región del usuario.

        Returns:
            int: La región del usuario.
        """
        # Pseudocódigo:
        # Retornar la región del usuario


    @region.setter
    def region(self, region) -> None:
        """
        Establece la región del usuario.

        Args:
            region (int): La región del usuario.
        """
        # Pseudocódigo:
        # Establecer la región del usuario
 

    # Requerimiento 5.4. Agregar método contestar_encuesta (se agrega implementación)
    def contestar_encuesta(self, encuesta: Union[Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion], respuestas: list) -> None:
        """
        Permite que el usuario conteste una encuesta.

        Args:
            encuesta (Union[Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion]): La encuesta a contestar.
            respuestas (list): Lista de respuestas del usuario.
        """
        # Pseudocódigo:
        # Crear una instancia de ListadoRespuestas con el usuario y sus respuestas
        # Llamar al método agregar_respuesta de la encuesta con el listado de respuestas

