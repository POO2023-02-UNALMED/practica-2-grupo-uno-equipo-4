from datetime import datetime

from ..usuarios.Empleado import Empleado
from ..usuarios.Usuario import Usuario
from ..hotel.Hotel import Hotel

#
# Clase CuentaBancaria
#
#       Hace referencia a la cuenta bancaria de un usuario o un hotel.
#       Dentro de ella se realizan acciones relacionadas con la cuenta 
#       bancaria, transacciones, consultas etc.+
#
#@autor: Camilo Sánchez
#

class CuentaBancaria():
    nCuentas = 1
    def __init__(self, saldo, banco, numero=None):

        if(numero == None):
            self.numero = self.nCuentas

        else:
            self.numero = numero

        self.saldo = saldo
        self.banco = banco
        self.ultimoPago = None

        CuentaBancaria.nCuentas += 1

    #
    # Método para transferir dinero desde la cuenta que lo llama 
    # hasta otra cuenta que se le pasa como paramatro.
    # El método actualiza la fecha del último pago
    #

    def transfarencia(self, cuenta, valor):
        self.retirar(valor)
        
        cuenta.depositar(valor)
        cuenta.setUltimoPago(datetime.now().date())
    
    #
    # Método estatico que transfiere dinero de dos cuentas bancarias que se le
    # pasan como parametro.
    # Después actualiza la fecha del último pago
    #

    @classmethod

    def transfarencia(cls, cuenta1, cuenta2, valor):

        cuenta1.retirar(valor)
        cuenta2.depositar(valor)
        cuenta2.setUltimoPago(datetime.now().date())
        
    def depositar(self, dinero):
        saldo = int(self.saldo)
        saldo += dinero
        self.saldo = saldo

    def retirar(self, dinero):
        saldo = int(self.saldo)
        saldo -= dinero
        self.saldo = saldo

    #
    # Método estatico que consulta si un hotel tiene saldo suficiente para hacer un
    # pago
    #

    @classmethod

    def puedePagarHotel(cls, hotel, pago):

        if hotel.getCuentaBancaria().getSaldo() >= pago:
            return True
        else:
            return False
        
    
    def getNumero(self):
        return self.numero
    
    def setNumero(self, numero):
        self.numero = numero

    def getBanco(self):
        return self.banco
    
    def setBanco(self, banco):
        self.banco = banco

    def getSaldo(self):
        return self.saldo
    
    def setSaldo(self, saldo):
        self.saldo = saldo

    def getUltimoPago(self):
        return self.ultimoPago
    
    def setUltimoPago(self, ultimoPago):
        self.ultimoPago = ultimoPago

    def getNCuentas(self):
        return self.nCuentas
    
    def setNCuentas(self, numero):
        self.nCuentas = numero