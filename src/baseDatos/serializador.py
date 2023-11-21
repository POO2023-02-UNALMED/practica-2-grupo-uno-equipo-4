import os
import pathlib
import pickle
from .Base import Base

#@autor: David Restrepo
# Esta clase se encarga de guardar la inforamción de los objetos que están en las listas de la clase Base

class Serializador:
    
    @classmethod
    def serializador(cls):
        path = os.path.join(pathlib.Path(__file__).parent.absolute())
        file = open(path+"\\temp\\administradores.pkl", "wb")
        pcs = Base.getAdministradores()
        pickle.dump(pcs, file)
        file.close()

        file = open(path+"\\temp\\huespedes.pkl", "wb")
        pcs = Base.getHuespedes()
        pickle.dump(pcs, file)
        file.close()

        file = open(path+"\\temp\\empleados.pkl", "wb")
        pcs = Base.getEmpleados()
        pickle.dump(pcs, file)
        file.close()

        file = open(path+"\\temp\\hoteles.pkl", "wb")
        pcs = Base.getHoteles()
        pickle.dump(pcs, file)
        file.close()