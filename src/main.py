from tkinter import Tk
from gestorGrafico.Root import Root
from gestorGrafico.Inicio import Inicio
from gestorGrafico.Recomendaciones import Recomendaciones
from gestorAplicacion.usuarios.Huesped import Huesped
from gestorAplicacion.hotel.Hotel import Hotel
from gestorAplicacion.hotel.Habitacion import Habitacion
from gestorAplicacion.usuarios.Preferencia import Preferencia
from gestorAplicacion.hotel.Reserva import Reserva
from gestorAplicacion.usuarios.Administrador import Administrador
from gestorAplicacion.usuarios.Empleado import Empleado
from baseDatos.deserealizador import Deserializador
from baseDatos.serializador import Serializador
from baseDatos.Base import Base
from gestorAplicacion.hotel.Hotel import Hotel
from gestorAplicacion.finanzas.CuentaBancaria import CuentaBancaria
from gestorAplicacion.hotel.Habitacion import Habitacion
from gestorAplicacion.hotel.TipoHabitacion import TipoHabitacion
from gestorAplicacion.usuarios.Huesped import Huesped
from gestorAplicacion.usuarios.Administrador import Administrador
from gestorAplicacion.usuarios.Empleado import Empleado
from gestorAplicacion.hotel.ServiciosExtra import ServiciosExtra

#@autor: David Restrepo


if __name__ == '__main__' :
    Deserializador.deserializador()

    # cuentaBancaria = CuentaBancaria(1000000, "b")
    # habitaciones = []
    # hab1 = Habitacion(1, "simple", TipoHabitacion.asign_camas(TipoHabitacion.SIMPLE), TipoHabitacion.asign_precio(TipoHabitacion.SIMPLE))
    # hab1.addCalificacion(Huesped(), 3)
    # hab1.addCalificacion(Huesped(), 2)
    # hab2 = Habitacion(2, "doble", TipoHabitacion.asign_camas(TipoHabitacion.DOBLE), TipoHabitacion.asign_precio(TipoHabitacion.DOBLE))
    # hab2.addCalificacion(Huesped(), 3)
    # hab2.addCalificacion(Huesped(), 3)
    # hab3 = Habitacion(3, "doblevip", TipoHabitacion.asign_camas(TipoHabitacion.VIPDOBLE), TipoHabitacion.asign_precio(TipoHabitacion.VIPDOBLE))
    # hab3.addCalificacion(Huesped(), 5)
    # hab3.addCalificacion(Huesped(), 5)
    # habitaciones.append(hab1)
    # habitaciones.append(hab2)
    # habitaciones.append(hab3)
    # hotel = Hotel(cuentaBancaria, "Hotel1", "Medellín", [], habitaciones, [])
    # Base.addHoteles(hotel)
    #PRUEBAS RECOMENDACIONES
    #habs = []
    #hab1 = Habitacion(1,"simple",1,1000)
    #hab2 = Habitacion(2,"doble",1,1000)
    #hab3 = Habitacion(3,"familiar",1,1000)
    #hab4 = Habitacion(4,"vipsimple",1,1000)
    #hab5 = Habitacion(5,"vipdoble",1,1000)
    #hab6 = Habitacion(6,"vipfamiliar",1,1000)
    #hab1.addCalificacion(Huesped(),0)
    #hab2.addCalificacion(Huesped(),1)
    #hab3.addCalificacion(Huesped(),2)
    #hab4.addCalificacion(Huesped(),3)
    #hab5.addCalificacion(Huesped(),4)
    #hab6.addCalificacion(Huesped(),5)
    #habs.append(hab1)
    #habs.append(hab2)
    #habs.append(hab3)
    #habs.append(hab4)
    #habs.append(hab5)
    #habs.append(hab6)
    #habs2 = []
    #hab10 = Habitacion(1,"simple",1,1000)
    #hab20 = Habitacion(2,"doble",1,1000)
    #hab30 = Habitacion(3,"familiar",1,1000)
    #hab40 = Habitacion(4,"vipsimple",1,1000)
    #hab50 = Habitacion(5,"vipdoble",1,1000)
    #hab60 = Habitacion(6,"vipfamiliar",1,1000)
    #hab10.addCalificacion(Huesped(),0)
    #hab20.addCalificacion(Huesped(),1)
    #hab30.addCalificacion(Huesped(),2)
    #hab40.addCalificacion(Huesped(),3)
    #hab50.addCalificacion(Huesped(),4)
    #hab60.addCalificacion(Huesped(),5)
    #habs2.append(hab10)
    #habs2.append(hab20)
    #habs2.append(hab30)
    #habs2.append(hab40)
    #habs2.append(hab50)
    #habs2.append(hab60)
    #hotel1 = Hotel(None,"Hotel","Medellin",None,habs,None)
    #hotel2 = Hotel(None,"Hotel1","Cali",None,habs,None)
    #hotel3 = Hotel(None,"Hotel2","Medellin",None,habs2,None)
    #Base.addHoteles(hotel1)
    #Base.addHoteles(hotel2)
    #Base.addHoteles(hotel3)
    #preferencias = []
    #preferencia = Preferencia("Medellin","Hotel",["vipsimple"])
    #preferencia2 = Preferencia("Medellin","Hotel2",["vipfamiliar","vipsimple"])
    #preferencias.append(preferencia2)
    #preferencias.append(preferencia)
    #huesped = Huesped(False,preferencias,"Alejandra",None,"Alejandra","123",None)
    #Base.addHuespedes(huesped)
    #reserva = Reserva(huesped,hab5,None,None,None,)
    #reserva.setCalificacionHotel(4)
    #huesped.addReserva(reserva)
    #hab5.addCalificacion(huesped,5)
    #reserva2 = Reserva(huesped,hab6,None,None,None)
    #reserva2.setCalificacionHotel(4)
    #huesped.addReserva(reserva2)
    #hab6.addCalificacion(huesped,5)
    #reserva3 = Reserva(huesped,hab60,None,None,None)
    #reserva3.setCalificacionHotel(4)
    #huesped.addReserva(reserva3)
    #hab60.addCalificacion(huesped,5)

    #Pruebas Administrador
    # cuentaBancariaH = CuentaBancaria(1000000, "b")
    # cuentaBancariaA = CuentaBancaria(1000000, "b")
    # cuentaBancariaE1 = CuentaBancaria(1000000, "b")
    # cuentaBancariaE2 = CuentaBancaria(1000000, "b")

    # habitaciones = []
    # hab1 = Habitacion(1, "simple", TipoHabitacion.asign_camas(TipoHabitacion.SIMPLE), TipoHabitacion.asign_precio(TipoHabitacion.SIMPLE))
    # hab1.addCalificacion(Huesped(), 3)
    # hab1.addCalificacion(Huesped(), 2)
    # hab2 = Habitacion(2, "doble", TipoHabitacion.asign_camas(TipoHabitacion.DOBLE), TipoHabitacion.asign_precio(TipoHabitacion.DOBLE))
    # hab2.addCalificacion(Huesped(), 3)
    # hab2.addCalificacion(Huesped(), 3)

    # habitaciones.append(hab1)
    # habitaciones.append(hab2)

    # hotel = Hotel(cuentaBancariaH, "Hotel1", "Medellín", [], habitaciones, [])

    # administrador1 = Administrador("Camilo", 12345, "kmi", "12345", cuentaBancariaA, hotel)

    # empleado1 = Empleado("Juan", 12344, "juanjo", "12345", cuentaBancariaE1, hotel, True, 3000)
    # empleado2 = Empleado("Carlos", 12333, "calitos", "12345", cuentaBancariaE2, hotel, True, 300)

    # Base.addHoteles(hotel)
    # Base.addAdministradores(administrador1)
    # Base.addEmpleados(empleado1)
    # Base.addEmpleados(empleado2)

    root = Root()
    Inicio(root)
    root.mainloop()

    Serializador.serializador()
    