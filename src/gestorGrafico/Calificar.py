import sys
from tkinter import Menu
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
from gestorGrafico.Usmenu import Usmenu

class Calificar :
    
    @classmethod
    def seleccionar(cls,root:Root,huesped=None):
        root.title("Calificar")
        menuBar = Menu(root)
        root.config(menu=menuBar)
        archivo = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Archivo", menu=archivo)
        archivo.add_command(label="Salir", command=root.salir)
        
        Titulo = tk.Label(root, text="Calificar", font=("arial", 25))
        subtitulo = tk.Label(root, text="A CONTINUACION SE  DESPLEGARAN 3 ENCUESTAS PARA CALIFICAR AL HOTEL", font=("arial", 15))
        Titulo.pack(side="top", padx=10, pady=10,)
        subtitulo.pack(side="top", padx=10, pady=10,)
        
        
        
        P1 = tk.Frame(root, bg="red")
        P1.pack(side="top", fill="both", expand=True)
        P2 = tk.Frame(P1, bg="yellow")
        P2.place(relx=0.5, rely=0.14, relheight=0.25, anchor="c")
        
        
        Titulo = tk.Label(P2, text="Habitacion", font=("arial", 15))
        Titulo.grid(row=0, column=0, padx=1, pady=1)
        
        etiqueta1 = tk.Label(P2, text="Ingrese un entero del  1 al 5, donde 1 es muy  insatisfecho y 5 es muy satisfecho", font=("arial", 10))
        etiqueta1.grid(row=1, column=0, padx=1, pady=1)
        
        types = [1,2,3,4,5]
        usType = Combobox(P2, values=types, state="readonly",font=("arial", 10))
        usType.set("Calificacion habitacion")
        usType.grid(row=1, column=1, padx=1, pady=1)
        #print(type(usType.get()))
        #3print(usType.get())
       # if int(usType.get()) < int(3):
        #    etiqueta4 = tk.Label(P2, text="Seleccione entre las siguiente opciones cual pudo haber sido  el  motivo de su mala experiencia", font=("arial", 10))
       #     etiqueta4.grid(row=2, column=0, padx=1, pady=1)
        #    types = ["Aseo Habitacion",
        #             "Iluminacion empleado",
        #             "Estado de los elementos de la habitacion",
        #             "Seguridad"]
        #    usType = Combobox(P2, values=types, state="readonly",font=("arial", 10))
        #    usType.set("Motivos")
        #    usType.grid(row=1, column=1, padx=1, pady=1)
        
        Titulo2 = tk.Label(P2, text="Empleado", font=("arial", 15))
        Titulo2.grid(row=3, column=0, padx=1, pady=1)
        
        etiqueta2 = tk.Label(P2, text="Seleccione un empleado a calificar", font=("arial", 10))
        etiqueta2.grid(row=4, column=0, padx=1, pady=1)
        cont = 1
        empleados = {}
        #for empleado in huesped.getReserva().getHotel().getEmpleados():
        #    empleados[empleado.getNombre()] = empleado
        usType2 = Combobox(P2, values=list(empleados.keys()), state="readonly",font=("arial", 10))
        usType2.set("Empleados")
        usType2.grid(row=4, column=1, padx=1, pady=1)
        
        etiqueta3 = tk.Label(P2, text="Ingrese un entero del  1 al 5, donde 1 es muy  insatisfecho y 5 es muy satisfecho", font=("arial", 10))
        etiqueta3.grid(row=5, column=0, padx=1, pady=1)
        
        types = [1,2,3,4,5]
        usType3 = Combobox(P2, values=types, state="readonly",font=("arial", 10))
        usType3.set("Calificacion empleado")
        usType3.grid(row=5, column=1, padx=1, pady=1)
        #username_label = tk.Label(P2, text="Ingrese su nombre de usuario:")
        #username_label.grid(row=1, column=0, padx=1, pady=1)
        #username_entry = tk.Entry(P2)
        #username_entry.grid(row=1, column=1, padx=1, pady=1)
    
   
        