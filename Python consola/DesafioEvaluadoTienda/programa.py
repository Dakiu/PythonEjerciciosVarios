
from tienda import TiendaRestaurante, TiendaSupermercado, TiendaFarmacia
from producto import Producto

# Solicitar el tipo de tienda a agregar, su nombre y costo de entrega
tipo = int(input("Ingrese tipo de la tienda a agregar:\n"
"1. Restaurante\n2. Supermercado\n3. Farmacia\n"))

nombre = input("\nIngrese nombre de la tienda a agregar:\n")
# Solicitar el costo de entrega de la tienda
precio_delivery = int(input("\nIngrese precio del delivery:\n"))

# Crear una instancia de la tienda correspondiente
if tipo == 2:
    # Si el tipo es 2, crear una tienda de supermercado
    tienda = TiendaSupermercado(nombre, precio_delivery)
elif tipo == 3:
    # Si el tipo es 3, crear una tienda de farmacia
    tienda = TiendaFarmacia(nombre, precio_delivery)
else:
    # Si el tipo es 1 o cualquier otro valor, crear una tienda de restaurante
    tienda = TiendaRestaurante(nombre, precio_delivery)

# Iniciar un ciclo para agregar productos a la tienda
opcion = 1
while opcion == 1:
    # Solicitar detalles del producto: nombre, precio y stock
    nombre_producto = input("\nIngrese nombre del producto a ingresar:\n")
    precio = int(input("\nIngrese precio del producto:\n"))
    stock = int(input("\nIngrese stock del producto:\n"))

    # Agregar el producto a la tienda
    tienda.ingresar_producto(nombre_producto, precio, stock)
    # Preguntar si el usuario quiere agregar otro producto
    opcion = int(input("\n¿Desea agregar otro producto?\n"
    "1. Sí\n2. No\n"))

# Preguntar qué quiere hacer el usuario a continuación: listar productos, realizar una venta o salir
opcion_productos = int(input("\nIndique qué desea realizar:\n"
"1. Listar productos de la tienda\n"
"2. Realizar una venta de producto\n"
"3. Salir\n"))

# Iniciar un ciclo para listar productos o realizar una venta
while opcion_productos in [1, 2]:
    if opcion_productos == 1:
        tienda.listar_productos()
    elif opcion_productos == 2:
        # Solicitar el nombre y la cantidad del producto a vender
        nombre_producto = input("\nIngrese nombre del producto a vender:\n")
        cantidad = int(input("\nIngrese cantidad que desea comprar:\n"))
        tienda.realizar_venta(nombre_producto, cantidad)
    
    # Preguntar nuevamente qué quiere hacer el usuario a continuación
    opcion_productos = int(input("\nIndique qué desea realizar:\n"
    "1. Listar productos de la tienda\n"
    "2. Realizar una venta de producto\n"
    "3. Salir\n"))
