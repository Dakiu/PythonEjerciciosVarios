
class Producto:
    # Constructor de la clase con atributos de instancia privados
    def __init__(self, nombre, precio, stock = 0):
        # Inicializar el nombre del producto
        self.__nombre = nombre  # Nombre del producto
        # Inicializar el precio del producto
        self.__precio = precio  # Precio del producto
        # Inicializar el stock del producto, debe ser mayor a 0
        self.__stock = stock if stock > 0 else 0  # Stock del producto

    @property
    def nombre(self):
      return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        if stock >=0:
            self.__stock = stock

    def __add__(self, other):
        pass

    def __sub__(self, other):
        # Sobrecargar el operador - para restar el stock de dos productos
        # Ingresa tu código aquí
        pass

    def __eq__(self, other):
        # Sobrecargar el operador == para comparar productos por nombre
        # Ingresa tu código aquí
        pass
