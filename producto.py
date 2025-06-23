class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(0, stock)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    def modificar_stock(self, cantidad):
        self.__stock = max(0, self.__stock + cantidad)

    def __eq__(self, otro):
        return self.__nombre == otro.nombre

    def __add__(self, otro):
        if self == otro:
            self.modificar_stock(otro.stock)
        return self

    def __sub__(self, cantidad):
        self.__stock = max(0, self.__stock - cantidad)
        return self