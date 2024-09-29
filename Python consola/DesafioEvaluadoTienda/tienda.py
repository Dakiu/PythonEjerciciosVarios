
from abc import ABC, abstractmethod
from producto import Producto

# Clase base abstracta para una tienda
class Tienda(ABC):
    @abstractmethod
    def ingresar_producto(self, nombre, precio, stock):
        # Método abstracto para agregar un producto
        pass

    @abstractmethod
    def listar_productos(self):
        # Método abstracto para listar productos
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        # Método abstracto para realizar una venta
        pass

# Clase concreta para una tienda de restaurante
class TiendaRestaurante(Tienda):
    # Tipo de tienda
    tipo = "Restaurante"

    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_producto(self, nombre, precio, stock):
        existe = False
        for item in self.__productos:
            if item.nombre == nombre:
                existe = True
                item.stock += stock
        
        miProducto = Producto(nombre, precio, 0) 
        if not existe:
            self.__productos.append(miProducto)

    def listar_productos(self):
        for item in self.__productos:
            print(f"Nombre: {item.nombre}, Precio: {item.precio}", "\n")

    def realizar_venta(self, nombre_producto, cantidad):
        pass
        

# Clase concreta para una tienda de farmacia
class TiendaFarmacia(Tienda):
    # Tipo de tienda
    tipo = "Farmacia"

    def __init__(self, nombre, costo_delivery):
        # Inicializar el nombre de la tienda
        self.__nombre = nombre
        # Inicializar el costo de entrega
        self.__costo_delivery = costo_delivery
        # Inicializar la lista de productos
        self.__productos = []

    def ingresar_producto(self, nombre, precio, stock):
        existe = False
        for item in self.__productos:
            if item.nombre == nombre:
                existe = True
                item.stock += stock
        
        miProducto = Producto(nombre, precio, stock) 
        if not existe:
            self.__productos.append(miProducto)

    def listar_productos(self):
        for item in self.__productos:
            mensaje=""
            if (item.precio>15000):
                mensaje="Envío gratis al solicitar este producto"
            print(f"Nombre: {item.nombre}, Precio: {item.precio} {mensaje}", "\n")

    def realizar_venta(self, nombre_producto, cantidad):

        if (cantidad <=3):
            for item in self.__productos:
                if item.nombre == nombre_producto and item.stock>=cantidad:
                    item.stock -= cantidad

# Clase concreta para una tienda de supermercado
class TiendaSupermercado(Tienda):
    # Tipo de tienda
    tipo = "Supermercado"

    def __init__(self, nombre, costo_delivery):
        # Inicializar el nombre de la tienda
        self.__nombre = nombre
        # Inicializar el costo de entrega
        self.__costo_delivery = costo_delivery
        # Inicializar la lista de productos
        self.__productos = []

    def ingresar_producto(self, nombre, precio, stock):
        
        existe = False
        for item in self.__productos:
            if item.nombre == nombre:
                existe = True
                item.stock += stock
        
        miProducto = Producto(nombre, precio, stock) 
        if not existe:
            self.__productos.append(miProducto)

    def listar_productos(self):
        
        for item in self.__productos:
            mensaje=""
            if (item.stock<10):
                mensaje="Pocos Productos Disponibles"
            print(f"Nombre: {item.nombre}, Precio: {item.precio}, Stock: {item.stock} {mensaje}", "\n")

    def realizar_venta(self, nombre_producto, cantidad):
        if (cantidad <=3):
            for item in self.__productos:
                if item.nombre == nombre_producto and item.stock>=cantidad:
                    item.stock -= cantidad

