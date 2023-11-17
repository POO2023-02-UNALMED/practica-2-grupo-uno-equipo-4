from enum import Enum

#@autor: David Restrepo

class TipoHabitacion(Enum):
    FAMILIAR = [4, 500000]
    DOBLE = [2, 300000]
    SIMPLE = [1, 100000]
    VIPFAMILIAR = [4, 1000000]
    VIPDOBLE = [2, 700000]
    VIPSIMPLE = [1, 300000]


    def asign_camas(tipo):
        return tipo.value[0]

    def asign_precio(tipo):
        return tipo.value[1]
    
if __name__ == "__main__":
    print(TipoHabitacion.asign_camas(TipoHabitacion.VIPFAMILIAR))