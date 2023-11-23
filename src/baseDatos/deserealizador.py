import os
import pathlib
import pickle
from .Base import Base

#@autor: David Restrepo

class Deserializador:
    
    @classmethod
    def deserializador(cls):
        file = open("C:/Users/Usuario/OneDrive/Escritorio/U/Cuarto Semestre/POO/Practica2/practica-2-grupo-uno-equipo-4/src/baseDatos/temp/administradores.pkl", "rb")
        try :
            pcs = pickle.load(file)
            Base.setAdministradores(pcs)
        except EOFError :
            Base.setAdministradores([])
        file.close()

        file = open("C:/Users/Usuario/OneDrive/Escritorio/U/Cuarto Semestre/POO/Practica2/practica-2-grupo-uno-equipo-4/src/baseDatos/temp/huespedes.pkl", "rb")
        try :
            pcs = pickle.load(file)
            Base.setHuespedes(pcs)
        except EOFError :
            Base.setHuespedes([])
        file.close()

        file = open("C:/Users/Usuario/OneDrive/Escritorio/U/Cuarto Semestre/POO/Practica2/practica-2-grupo-uno-equipo-4/src/baseDatos/temp/hoteles.pkl", "rb")
        try :
            pcs = pickle.load(file)
            Base.setHoteles(pcs)
        except EOFError :
            Base.setHoteles([])
        file.close()

        file = open("C:/Users/Usuario/OneDrive/Escritorio/U/Cuarto Semestre/POO/Practica2/practica-2-grupo-uno-equipo-4/src/baseDatos/temp/empleados.pkl", "rb")
        try :
            pcs = pickle.load(file)
            Base.setEmpleados(pcs)
        except EOFError :
            Base.setEmpleados([])
        file.close()

