import os
import pathlib
import pickle
from .Base import Base

#@autor: David Restrepo

class Deserializador:
    
    @classmethod
    def deserializador(cls):
        path = os.path.join(pathlib.Path(__file__).parent.absolute())
        file = open(path+"\\temp\\administradores.pkl", "rb")
        try :
            pcs = pickle.load(file)
            Base.setAdministradores(pcs)
        except EOFError :
            Base.setAdministradores([])
        file.close()

        file = open(path+"\\temp\\huespedes.pkl", "rb")
        try :
            pcs = pickle.load(file)
            Base.setHuespedes(pcs)
        except EOFError :
            Base.setHuespedes([])
        file.close()

        file = open(path+"\\temp\\hoteles.pkl", "rb")
        try :
            pcs = pickle.load(file)
            Base.setHoteles(pcs)
        except EOFError :
            Base.setHoteles([])
        file.close()

        file = open(path+"\\temp\\empleados.pkl", "rb")
        try :
            pcs = pickle.load(file)
            Base.setEmpleados(pcs)
        except EOFError :
            Base.setEmpleados([])
        file.close()

