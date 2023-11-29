import pickle
from .Base import Base

#@autor: David Restrepo
class Serializador:
    @classmethod
    def serializador(cls):
        file = open("C:/Users/Usuario/OneDrive/Escritorio/U/Cuarto Semestre/POO/Practica2/practica-2-grupo-uno-equipo-4/src/baseDatos/temp/administradores.pkl", "wb")
        pcs = Base.getAdministradores()
        pickle.dump(pcs, file)
        file.close()

        file = open("C:/Users/Usuario/OneDrive/Escritorio/U/Cuarto Semestre/POO/Practica2/practica-2-grupo-uno-equipo-4/src/baseDatos/temp/huespedes.pkl", "wb")
        pcs = Base.getHuespedes()
        pickle.dump(pcs, file)
        file.close()

        file = open("C:/Users/Usuario/OneDrive/Escritorio/U/Cuarto Semestre/POO/Practica2/practica-2-grupo-uno-equipo-4/src/baseDatos/temp/empleados.pkl", "wb")
        pcs = Base.getEmpleados()
        pickle.dump(pcs, file)
        file.close()

        file = open("C:/Users/Usuario/OneDrive/Escritorio/U/Cuarto Semestre/POO/Practica2/practica-2-grupo-uno-equipo-4/src/baseDatos/temp/hoteles.pkl", "wb")
        pcs = Base.getHoteles()
        pickle.dump(pcs, file)
        file.close()