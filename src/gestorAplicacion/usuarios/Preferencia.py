class Preferencia:
    def __init__(self,ciudad=None,nombreHotel=None,tipoHabitacion=None):
        if ciudad is not None:
            self._ciudad = ciudad
        if nombreHotel is not None:
            self._nombreHotel = nombreHotel

        if tipoHabitacion is not None:
            self._tipoHabitacion = tipoHabitacion