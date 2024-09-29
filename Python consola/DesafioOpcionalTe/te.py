# Paso 1: Definir la clase Te
class Te:
    # Atributo de clase que define la duración en días
    duracion = 365

    def __init__(self, sabor, formato, preparacion, recomendacion) -> None:
        self.sabor = sabor
        self.formato = formato
        self.preparacion = preparacion
        self.recomendacion = recomendacion

    # Paso 2: Método estático que retorna tiempo de preparación y recomendación según el sabor
    @staticmethod
    def retorna_tiempo_y_recomendacion(sabor: int):
        """
        Retorna el tiempo de preparación y la recomendación de consumo basado en el sabor.

        Parámetros:
        sabor (int): Número entero que representa el sabor del té (1, 2 o 3).

        Retorna:
        tuple: Tiempo de preparación (int) y recomendación de consumo (str).
        """
        # ingresa tu código acá
        
        if sabor==1:
            preparacion = 3
            recomendacion = "desayuno"
        elif sabor == 2:
            preparacion = 5
            recomendacion = "mediodia"
        else:
            preparacion = 6
            recomendacion = "atardecer"

        return preparacion,recomendacion

    # Paso 3: Método estático que retorna el precio según el formato
    @staticmethod
    def retorna_precio(formato: int):
        """
        Retorna el precio del té basado en el formato.

        Parámetros:
        formato (int): Número entero que representa el formato en gramos (300 o 500).

        Retorna:
        int: Precio del té en pesos.
        """
        precio = 0
        if formato == 300:
            precio = 3000
        elif formato == 500:
            precio = 5000
        # ingresa tu código acá
        return precio
