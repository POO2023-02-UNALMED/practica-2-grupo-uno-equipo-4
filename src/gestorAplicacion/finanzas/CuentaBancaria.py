class CuentaBancaria():
    numeroCuentas = 0
    def __init__(self, numero, saldo, banco):

        self.numero = numero
        self.saldo = saldo
        self.banco = banco
        self.ultimoPago = None

        numeroCuentas += 1