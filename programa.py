from tienda import Restaurante, Supermercado, Farmacia

tipo = input("Ingrese tipo de tienda (Restaurante/Supermercado/Farmacia): ").lower()
nombre = input("Nombre de la tienda: ")
delivery = int(input("Costo de delivery: "))

# 3 tipos de tiendas disponibles
if tipo == "restaurante":
    tienda = Restaurante(nombre, delivery)
elif tipo == "supermercado":
    tienda = Supermercado(nombre, delivery)
elif tipo == "farmacia":
    tienda = Farmacia(nombre, delivery)
else:
    print("Tipo de tienda no válido")
    exit()

while True:
    opc = input("¿Desea ingresar un producto? (s/n): ").lower()
    if opc != 's':
        break
    nombre_p = input("Nombre del producto: ")
    precio = int(input("Precio: "))
    stock = int(input("Stock (opcional, 0 por defecto): ") or 0)
    tienda.ingresar_producto(nombre_p, precio, stock)

while True:
    #menu de opciones
    print("Opciones:")
    print("1. Listar productos")
    print("2. Realizar venta")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Productos:")
        print(tienda.listar_productos())
    elif opcion == "2":
        nombre_v = input("Nombre del producto a vender: ")
        cantidad = int(input("Cantidad: "))
        tienda.realizar_venta(nombre_v, cantidad)
    elif opcion == "3":
        break
    else:
        print("Opción no válida")
