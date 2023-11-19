from datetime import datetime

from .Usuario import Usuario
from ..hotel.Hotel import Hotel
from ..hotel.Habitacion import Habitacion
from ..finanzas.CuentaBancaria import CuentaBancaria

#
# Clase administrador
#
#       La clase administrador hereda de la clase usuario.
#       Un administrador será un usuario con más permisos
#       dentro del programa
#
#@autor: Camilo Sánchez
#

class Administrador(Usuario):

    totalAdministradores = 0

    def __init__(self, nombre, telefono, usuario, password, cuentaBancaria, hotel):

        super().__init__(nombre, telefono, usuario, password, cuentaBancaria)
        
        self.hotel = hotel
        self.salario = 500
        self.ultimoPago = None
        Administrador.totalAdministradores += 1

    def crearAdministrador(self, nombre, telefono, usuario, password, cuentaBancaria, hotel):

        administradorCreado = Administrador(nombre, telefono, usuario, password, cuentaBancaria, hotel)

        return administradorCreado
    
    def premiarUsuario():
        pass

    def hacerDescuento():
        pass

    def cobrarZonas():
        pass

    def agregarServicio():
        pass

    def alterarServicio():
        pass

    def calcularPromedio():
        pass

    #Crea una habitación dependiendo el TipoHabitacion (Enum)

    def administradorAgregaHabitacion(self, tipoEscogido):
        pass

    def listarAdministradores(self):

        administradores = ""
        contador = 1

        for administrador in self.hotel.getAdministradores():
            administradores += "    " + str(contador) + ". " + administrador
            contador += 1

        return administradores
    
    def ultimoMesPago(self):
        return self.getCuentaBancaria().getUltimoPago()
    
    def dineroCuentaHotel(self):
        return self.hotel.getCuentaBancaria().getSaldo()
    
    #
    # Devuelve true si el hotel tiene el suficiente dinero en cuenta
    # para pagarle a sus empleados y administradores. Llama al método de
    # la cuenta banacaria para hacer la consulta
    #

    def puedePagarHotel(self, empleados):

        saldoAPagar = 0

        for empleado in empleados:
            saldoAPagar += empleado.getSalario()

        saldoAPagar += self.salario

        return CuentaBancaria.puedePagarHotel(self.hotel, saldoAPagar)
    
    #
    # Primero consulta si el último pago se realizó hace más de 30 días,
    # después consulta si el hotel tiene el dinero suficiente en cuenta
    # para pagarle a los empleados, si las dos condiciones se cumplen le realiza el pago
    # a los empleados
    #

    def pagarEmpleados(self):

        empleados = self.hotel.getEmpleado()

        ultimoPago = self.getUltimoPago()
        actual = datetime.now().date()

        diferienciaDias = 0

        for empleado in empleados:

            if(empleado.getUltimoPago() == None) or (self.getUltimoPago == None):
                
                diferienciaDias = 40

            else:

                diferienciaDias = (actual - ultimoPago).days

        if diferienciaDias < 30:
            return 1
        
        else:

            if (self.puedePagarHotel(empleados)):

                for empleado in empleados:
                    CuentaBancaria.transfarencia(self.hotel.getCuentaBancaria(), empleado.getCuentaBancaria(), empleado.getSalario())
                    empleado.setUltimoPago(actual)

                CuentaBancaria.transfarencia(self.getHotel().getCuentaBancaria(), self.getCuentaBancaria(), self.getSalario())
                self.setUltimoPago(actual)

                return 0
            
            else:
                return 2
            
    def saldoAPagarHotel(self, empleados):

        saldoAPagar = 0

        for empleado in empleados:
            saldoAPagar += empleado.getSalario()

        saldoAPagar += self.salario

        return saldoAPagar


    def reiniciarUltimoPago(self):

        empleados = self.getHotel().getEmpleado()

        for empleado in empleados:
            empleado.setUltimoPago(None)

        self.setUltimoPago(None)


    def getTotalAdministradores(self):
        return self.totalAdministradores
    
    def getHotel(self):
        return self.hotel
    
    def setHotel(self, hotel):
        self.hotel = hotel

    def getSalario(self):
        return self.salario
    
    def setSalario(self, salario):
        self.salario = salario

    def aumentoSalario(self, aumento):
        self.salario += aumento

    def getUltimoPago(self):
        return self.ultimoPago
    
    def setUltimoPago(self, ultimoPago):
        self.ultimoPago = ultimoPago

    def presentacion(self):
        return ""

    def entrando(self):
        return f"Entrando a su cuenta de Administrador, señor(a): {self.getNombre()}"