from .Usuario import Usuario

class Administrador(Usuario):

    totalAdministradores = 0

    def __init__(self, nombre, telefono, usuario, password, cuentaBancaria, hotel):

        super().__init__(nombre, telefono, usuario, password, cuentaBancaria)
        self.hotel = hotel
        self. salario = 500
        self.ultimoPago = None
        totalAdministradores += 1