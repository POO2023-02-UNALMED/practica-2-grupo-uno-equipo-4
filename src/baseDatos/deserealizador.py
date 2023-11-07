import pickle
from .Base import Base

class Deserializador:
    @classmethod
    def deserializador(cls):
        file = open("baseDatos/temp/administradores.pkl", "rb")
        try :
            pcs = pickle.load(file)
            Base.setProfesores(pcs)
        except EOFError :
            Base.setProfesores([])
        file.close()

        file = open("baseDatos/temp/huespedes.pkl", "rb")
        try :
            pcs = pickle.load(file)
            Base.setEstudiantes(pcs)
        except EOFError :
            Base.setEstudiantes([])
        file.close()

        file = open("baseDatos/temp/hoteles.pkl", "rb")
        try :
            pcs = pickle.load(file)
            Base.setAdmins(pcs)
        except EOFError :
            Base.setAdmins([])
        file.close()

        file = open("baseDatos/temp/empleados.pkl", "rb")
        try :
            pcs = pickle.load(file)
            Base.setEstudiantesMatriculados(pcs)
        except EOFError :
            Base.setEstudiantesMatriculados([])
        file.close()

