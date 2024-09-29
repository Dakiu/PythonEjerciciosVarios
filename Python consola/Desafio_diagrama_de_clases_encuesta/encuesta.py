# Requerimiento 4.1. Importar la clase Pregunta, y definir la clase Encuesta
from pregunta import Pregunta
from typing import List

class Encuesta:
    """
    Clase que representa una encuesta.

    Atributos:
        nombre (str): El nombre de la encuesta.
        preguntas (list): Lista de preguntas de la encuesta.
        listados_respuestas (list): Lista de listados de respuestas a la encuesta.
    """

    # Requerimiento 4.2. Definir el constructor con los atributos de instancia indicados en el diagrama
    def __init__(self, nombre: str, preguntas: List[dict]) -> None:
        """
        Inicializa una instancia de la clase Encuesta.

        Args:
            nombre (str): El nombre de la encuesta.
            preguntas (list): Lista de diccionarios con preguntas.
        """
        # Pseudocódigo:
        # Establecer el nombre de la encuesta
        # Crear una lista de instancias de la clase Pregunta a partir de la lista de preguntas
        # Inicializar la lista de listados de respuestas
        self.nombre = nombre
        self.__preguntas = [Pregunta(p["enunciado"], p["ayuda"], p["alternativas"], p["requerido"]) for p in preguntas]
        self.__listados_respuestas = []

    # Requerimiento 4.3. Agregar método mostrar_encuesta (se agrega implementación)
    def mostrar_encuesta(self) -> None:
        """
        Muestra el nombre de la encuesta y todas sus preguntas.
        """
        # Pseudocódigo:
        # Imprimir el nombre de la encuesta
        # Para cada pregunta en la lista de preguntas, llamar al método mostrar_pregunta
        print(self.nombre)
        for p in self.__preguntas:
            p.mostrar_pregunta()

    # Requerimiento 4.4. Agregar método agregar_listado_respuestas (se agrega implementación)
    def agregar_listado_respuestas(self, listado_respuestas) -> None:
        """
        Agrega un listado de respuestas a la encuesta.

        Args:
            listado_respuestas (ListadoRespuestas): El listado de respuestas a agregar.
        """
        # Pseudocódigo:
        # Agregar el listado de respuestas a la lista de listados de respuestas
        self.__listados_respuestas.append(listado_respuestas)

# Requerimiento 4.5. En el mismo archivo, agregar clase EncuestaLimitadaEdad, que hereda de Encuesta.
# En el constructor, llamar al de la clase padre, y agregar atributos propios.
class EncuestaLimitadaEdad(Encuesta):
    """
    Clase que representa una encuesta limitada por edad.

    Atributos:
        edad_min (int): La edad mínima permitida para responder la encuesta.
        edad_max (int): La edad máxima permitida para responder la encuesta.
    """

    def __init__(self, nombre: str, preguntas: list, edad_min: int, edad_max: int) -> None:
        """
        Inicializa una instancia de la clase EncuestaLimitadaEdad.

        Args:
            nombre (str): El nombre de la encuesta.
            preguntas (list): Lista de diccionarios con preguntas.
            edad_min (int): La edad mínima permitida para responder la encuesta.
            edad_max (int): La edad máxima permitida para responder la encuesta.
        """
        # Pseudocódigo:
        # Llamar al constructor de la clase padre (Encuesta)
        # Establecer la edad mínima permitida
        # Establecer la edad máxima permitida
        super().__init__(nombre, preguntas)
        self.__edad_min = edad_min
        self.__edad_max = edad_max

    # Requerimiento 4.6. Agregar propiedades de atributos propios
    @property
    def edad_min(self) -> int:
        """
        Devuelve la edad mínima permitida para responder la encuesta.

        Returns:
            int: La edad mínima permitida.
        """
        # Pseudocódigo:
        # Retornar la edad mínima permitida
        return self.__edad_min

    @edad_min.setter
    def edad_min(self, edad_min) -> None:
        """
        Establece la edad mínima permitida para responder la encuesta.

        Args:
            edad_min (int): La edad mínima permitida.
        """
        # Pseudocódigo:
        # Establecer la edad mínima permitida
        self.__edad_min = edad_min

    @property
    def edad_max(self) -> int:
        """
        Devuelve la edad máxima permitida para responder la encuesta.

        Returns:
            int: La edad máxima permitida.
        """
        # Pseudocódigo:
        # Retornar la edad máxima permitida
        return self.__edad_max

    @edad_max.setter
    def edad_max(self, edad_max) -> None:
        """
        Establece la edad máxima permitida para responder la encuesta.

        Args:
            edad_max (int): La edad máxima permitida.
        """
        # Pseudocódigo:
        # Establecer la edad máxima permitida
        self.__edad_max = edad_max

    # Requerimiento 4.7. Sobrescribir el método para agregar_respuesta (se agrega implementación)
    def agregar_respuesta(self, respuestas: 'ListadoRespuestas') -> None:
        """
        Agrega un listado de respuestas a la encuesta si el usuario cumple con la restricción de edad.

        Args:
            respuestas (ListadoRespuestas): El listado de respuestas a agregar.
        """
        # Pseudocódigo:
        # Si la edad del usuario está entre la edad mínima y la edad máxima permitida
        # entonces agregar el listado de respuestas
        if self.__edad_min <= respuestas.usuario.edad <= self.__edad_max:
            super().agregar_listado_respuestas(respuestas)

# Requerimiento 4.8. Definir luego la clase EncuestaLimitadaRegion, que hereda de Encuesta. En su constructor,
# luego de llamar al constructor padre asigna los atributos propios.
class EncuestaLimitadaRegion(Encuesta):
    """
    Clase que representa una encuesta limitada por región.

    Atributos:
        regiones (list): Lista de regiones permitidas para responder la encuesta.
    """

    def __init__(self, nombre: str, preguntas: list, regiones: List[int]) -> None:
        """
        Inicializa una instancia de la clase EncuestaLimitadaRegion.

        Args:
            nombre (str): El nombre de la encuesta.
            preguntas (list): Lista de diccionarios con preguntas.
            regiones (list): Lista de regiones permitidas.
        """
        # Pseudocódigo:
        # Llamar al constructor de la clase padre (Encuesta)
        # Establecer la lista de regiones permitidas
        super().__init__(nombre, preguntas)
        self.__regiones = regiones

    # Requerimiento 4.9. Agregar propiedad para regiones
    @property
    def regiones(self) -> List[int]:
        """
        Devuelve la lista de regiones permitidas para responder la encuesta.

        Returns:
            list: Lista de regiones permitidas.
        """
        # Pseudocódigo:
        # Retornar la lista de regiones permitidas
        return self.__regiones

    @regiones.setter
    def regiones(self, regiones) -> None:
        """
        Establece la lista de regiones permitidas para responder la encuesta.

        Args:
            regiones (list): Lista de regiones permitidas.
        """
        # Pseudocódigo:
        # Establecer la lista de regiones permitidas
        self.__regiones = regiones

    # Requerimiento 4.10. Sobrescribir el método agregar_respuesta (se agrega implementación)
    def agregar_respuesta(self, respuestas: 'ListadoRespuestas') -> None:
        """
        Agrega un listado de respuestas a la encuesta si el usuario cumple con la restricción de región.

        Args:
            respuestas (ListadoRespuestas): El listado de respuestas a agregar.
        """
        # Pseudocódigo:
        # "Si" la región del usuario está en la lista de regiones permitidas
        # entonces agregar el listado de respuestas

