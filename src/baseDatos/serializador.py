import pickle
from .Base import Base

class Serializador:
    @classmethod
    def serializador(cls):
        file = open("baseDatos/temp/administradores.pkl", "wb")
        pcs = Base.getAdministradores()
        pickle.dump(pcs, file)
        file.close()

        file = open("baseDatos/temp/huespedes.pkl", "wb")
        pcs = Base.getHuespedes()
        pickle.dump(pcs, file)
        file.close()

        file = open("baseDatos/temp/empleados.pkl", "wb")
        pcs = Base.getEmpleados()
        pickle.dump(pcs, file)
        file.close()

        file = open("baseDatos/temp/hoteles.pkl", "wb")
        pcs = Base.getHoteles()
        pickle.dump(pcs, file)
        file.close()