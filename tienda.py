from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    #constructor
    def __init__(self, nombre, costo_delivery):
        self._nombre = nombre
        self._costo_delivery = costo_delivery
        self._productos = []

    def ingresar_producto(self, nombre, precio, stock=0):
        nuevo = Producto(nombre, precio, stock)

        for p in self._productos:
            if p == nuevo:
                if isinstance(self, Restaurante):
                    return
                p + nuevo
                return

        if isinstance(self, Restaurante):
            nuevo = Producto(nombre, precio, 0)

        self._productos.append(nuevo)

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre, cantidad):
        pass


class Restaurante(Tienda):
    def listar_productos(self):
        lista = []
        for p in self._productos:
            linea = f"{p.nombre} - ${p.precio}"
            lista.append(linea)
        return "\n".join(lista)

    def realizar_venta(self, nombre, cantidad):
        for p in self._productos:
            if p.nombre == nombre:
                print(f"Venta realizada: {cantidad} x {p.nombre}")
                return


class Supermercado(Tienda):
    def listar_productos(self):
        lista = []
        for p in self._productos:
            linea = f"{p.nombre} - ${p.precio}"
            if p.stock < 10:
                linea += f" - Stock: {p.stock} (Pocos productos disponibles)"
            else:
                linea += f" - Stock: {p.stock}"
            lista.append(linea)
        return "\n".join(lista)

    def realizar_venta(self, nombre, cantidad):
        for p in self._productos:
            if p.nombre == nombre and p.stock > 0:
                vendidos = min(p.stock, cantidad)
                p - vendidos
                print(f"Venta realizada: {vendidos} x {p.nombre}")
                return


class Farmacia(Tienda):
    def listar_productos(self):
        lista = []
        for p in self._productos:
            linea = f"{p.nombre} - ${p.precio}"
            if p.precio > 15000:
                linea += " - Envío gratis al solicitar este producto"
            lista.append(linea)
        return "\n".join(lista)

    def realizar_venta(self, nombre, cantidad):
        if cantidad > 3:
            return
        for p in self._productos:
            if p.nombre == nombre and p.stock > 0:
                vendidos = min(p.stock, cantidad)
                p - vendidos
                print(f"Venta realizada: {vendidos} x {p.nombre}")
                return