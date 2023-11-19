from tkinter import Tk
from gestorGrafico.Root import Root
from gestorGrafico.Inicio import Inicio
from gestorGrafico.Recomendaciones import Recomendaciones
from gestorAplicacion.usuarios.Huesped import Huesped
from gestorAplicacion.hotel.Hotel import Hotel
from gestorAplicacion.hotel.Habitacion import Habitacion
from gestorAplicacion.usuarios.Preferencia import Preferencia
from gestorAplicacion.hotel.Reserva import Reserva
from baseDatos.deserealizador import Deserializador
from baseDatos.serializador import Serializador
from baseDatos.Base import Base
from gestorAplicacion.hotel.Hotel import Hotel
from gestorAplicacion.finanzas.CuentaBancaria import CuentaBancaria
from gestorAplicacion.hotel.Habitacion import Habitacion
from gestorAplicacion.hotel.TipoHabitacion import TipoHabitacion
from gestorAplicacion.usuarios.Huesped import Huesped

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
    root = Root()
    Inicio(root)
    root.mainloop()

    Serializador.serializador()
    