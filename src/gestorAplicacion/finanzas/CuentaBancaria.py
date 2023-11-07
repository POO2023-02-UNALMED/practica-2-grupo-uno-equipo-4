class CuentaBancaria():
    numeroCuentas = 1
    def __init__(self, saldo, banco):

        self.numero = CuentaBancaria.numeroCuentas
        self.saldo = saldo
        self.banco = banco
        self.ultimoPago = None

        CuentaBancaria.numeroCuentas += 1
        
    def depositar(self, dinero):
        saldo = int(self.saldo)
        saldo += dinero
        self.saldo = saldo

    def retirar(self, dinero):
        saldo = int(self.saldo)
        saldo -= dinero
        self.saldo = saldo