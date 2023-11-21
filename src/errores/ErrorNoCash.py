from .ErrorReserv import ErrorReserv

#@autor: David Restrepo
# Esta clase se encarga de controlar los errores cuando no hay saldo suficeinte al momento de realizar la reserva

class ErrorNoCash(ErrorReserv):
    def __init__(self, saldo, precio):
        super().__init__(f"Su saldo: {saldo} no es suficiente para el siguiente gasto: {precio}")
        self.saldo = saldo
        self.precio = precio
        
    def mostrarMensaje(self):
        return  (f"Su saldo: {self.saldo} no es suficiente para el siguiente gasto: {self.precio}")