import sys
from tkinter import Button, Menu
import tkinter as tk
from tkinter.ttk import Combobox
from gestorGrafico import Root
from baseDatos.Base import Base
from gestorAplicacion.usuarios.Preferencia import Preferencia
from gestorAplicacion.usuarios.Huesped import Huesped
from gestorAplicacion.finanzas.CuentaBancaria import CuentaBancaria
from gestorAplicacion.hotel.Hotel import Hotel
from gestorAplicacion.usuarios.Administrador import Administrador
from gestorAplicacion.usuarios.Empleado import Empleado

#@autor: David Restrepo

class Usmenu():    
    
    @classmethod
    def menu(cls, root:Root, us):   
        root.title("CosmoReserve")
        menuBar = Menu(root)
        root.config(menu=menuBar)
        
        archivo = Menu(menuBar, tearoff=False)                              #opcion archivo 
        menuBar.add_cascade(label="Archivo", menu=archivo)
        archivo.add_command(label="Aplicación", command=root.aplicacion)
        archivo.add_command(label="Salir", command=root.salir)
        
        prosCon = Menu(menuBar, tearoff=False)                           #opcion procesos y consultas
        menuBar.add_cascade(label="Procesos y Consultas", menu=prosCon)
        
        ayuda = Menu(menuBar, tearoff=False)                           #opcion ayuda
        menuBar.add_cascade(label="Ayuda", menu=ayuda)
        ayuda.add_command(label="Acerca de", command=root.ayuda)
        
        
        if isinstance(us, Huesped):
            cls.sistemaHuesped(root, us, prosCon)
        elif isinstance(us, Administrador):
            cls.sistemaAdministrador(root, us, prosCon)
        else:
            cls.sistemaEmpleado(root, us, prosCon)
            
    @classmethod
    def sistemaHuesped(cls, root, us, prosCon):
        pass
        
    @classmethod
    def sistemaAdministrador(cls, root, us, prosCon):
        pass
        
    @classmethod
    def sistemaEmpleado(cls, root, us, prosCon):
        pass