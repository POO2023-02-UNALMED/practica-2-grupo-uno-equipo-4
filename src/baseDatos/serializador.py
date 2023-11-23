import pickle
from .Base import Base

#@autor: David Restrepo
class Serializador:
    @classmethod
    def serializador(cls):
        file = open("src/baseDatos/temp/administradores.pkl", "wb")
        pcs = Base.getAdministradores()
        pickle.dump(pcs, file)
        file.close()

        file = open("src/baseDatos/temp/huespedes.pkl", "wb")
        pcs = Base.getHuespedes()
        pickle.dump(pcs, file)
        file.close()

        file = open("src/baseDatos/temp/hoteles.pkl", "wb")
        pcs = Base.getEmpleados()
        pickle.dump(pcs, file)
        file.close()

        file = open("src/baseDatos/temp/empleados.pkl", "wb")
        pcs = Base.getHoteles()
        pickle.dump(pcs, file)
        file.close()