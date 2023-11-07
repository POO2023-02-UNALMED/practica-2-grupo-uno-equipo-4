from .Usuario import Usuario

class Administrador(Usuario):

    totalAdministradores = 0

    def __init__(self, nombre, telefono, usuario, password, cuentaBancaria, hotel):

        super().__init__(nombre, telefono, usuario, password, cuentaBancaria)
        self.hotel = hotel
        self. salario = 500
        self.ultimoPago = None
        Administrador.totalAdministradores += 1
        
    def presentacion(self):
        return ""

    def entrando(self):
        return f"Entrando a su cuenta de Administrador, señor(a): {self.getNombre()}"