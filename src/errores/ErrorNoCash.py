from .ErrorReserv import ErrorReserv

#@autor: David Restrepo

class ErrorNoCash(ErrorReserv):
    def __init__(self, saldo, precio):
        super().__init__(f"Su saldo: {saldo} no es suficiente para el siguiente gasto: {precio}")
        self.saldo = saldo
        self.precio = precio
        
    def mostrarMensaje(self):
        return  (f"Su saldo: {self.saldo} no es suficiente para el siguiente gasto: {self.precio}")