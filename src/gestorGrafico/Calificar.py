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
from gestorAplicacion.hotel.ServiciosExtra import ServiciosExtra
from tkinter import Menu, messagebox

class Calificar :

    
    
    @classmethod
    def seleccionar(cls,root:Root,huesped:Huesped):
        
        def verificar(huesped):
            #print(type(usType.get()))
            #print(usType2.get())
            #print(usType5.get())
            #print(diccionario)
            if int(usType.get()) in types and usType2.get() in empleados.keys() and int(usType3.get()) in types and usType6.get() in servicios.keys()  and int(usType5.get()) in types:
                #huesped.getReserva().getHabitacion().addCalificacion(huesped,int(usType))
                
                print(huesped.getReserva().getHotel().getEmpleados())
                for i in huesped.getReserva().getHotel().getEmpleados():
                    print("entro")
                    if  i.getNombre() == usType2:
                        i.addCalificacion(huesped,int(usType3))
                        print(i.getCalificaciones())
                for i in huesped.getReserva().getHotel().getServicios():
                    if  i.getNombre() == usType6:
                        i.addCalificacion(huesped,int(usType5))
                        print(i.getCalificaciones())
                print("calculau")
                
            else:
                messagebox.showerror("Llene todos los campos")
        
        root.title("Calificar")
        menuBar = Menu(root)
        root.config(menu=menuBar)
        archivo = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Archivo", menu=archivo)
        archivo.add_command(label="Salir", command=root.salir)
        
        Titulo = tk.Label(root, text="Calificar", font=("arial", 25))
        subtitulo = tk.Label(root, text="A CONTINUACION SE DESPLEGARA LA ENCUESTA PARA CALIFICAR AL HOTEL", font=("arial", 15))
        Titulo.pack(side="top", padx=10, pady=10,)
        subtitulo.pack(side="top", padx=10, pady=10,)
        
        
        
        P1 = tk.Frame(root, bg="red")
        P1.pack(side="top", fill="both", expand=True)
        P2 = tk.Frame(P1, bg="yellow")
        P2.place(relx=0.5, relheight=0.5, anchor="n")
        
        
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
        #print(huesped.getReserva().getHotel().getEmpleados()[0])
        for empleado in huesped.getReserva().getHotel().getEmpleados():
            empleados[empleado.getNombre()] = empleado
        usType2 = Combobox(P2, values=list(empleados.keys()), state="readonly",font=("arial", 10))
        usType2.set("Empleados")
        usType2.grid(row=4, column=1, padx=1, pady=1)
        
        #while usType2 not in empleados.keys():
         #   usType2 = Combobox(P2, values=list(empleados.keys()), state="readonly",font=("arial", 10))
          #  usType2.set("Empleados")
           # usType2.grid(row=4, column=1, padx=1, pady=1)
            #messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")
        
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
        conts = 7
        #print(huesped.getReserva())
        # serv1 = ServiciosExtra(1)
        # serv1.setTipoServicio("Piscina")
        # serv2 = ServiciosExtra(2)
        # serv2.setTipoServicio("Transporte")
        # serv3 = ServiciosExtra(3)
        # serv3.setTipoServicio("Teatro")
        # print(serv3.getTipoServicio())
        #servicios = [serv1,serv2,serv3]
        Titulo2 = tk.Label(P2, text="Servicios", font=("arial", 15))
        Titulo2.grid(row=6, column=0, padx=1, pady=1)
        #for servicio  in servicios:
        servicios = {}
        for servicio in huesped.getReserva().getHotel().getServicios():
            servicios[servicio.getNombre()]=servicio
        
        etiqueta6 = tk.Label(P2, text="Seleccione un servicio a calificar", font=("arial", 10))
        etiqueta6.grid(row=7, column=0, padx=1, pady=1)
        usType6 = Combobox(P2, values=list(servicios.keys()), state="readonly",font=("arial", 10))
        usType6.set("servicio")
        usType6.grid(row=7, column=1, padx=1, pady=1)
        
        etiqueta4 = tk.Label(P2, text="Ingrese un entero del  1 al 5, donde 1 es muy  insatisfecho y 5 es muy satisfecho", font=("arial", 10))
        etiqueta4.grid(row=8, column=0, padx=1, pady=1)
        types = [1,2,3,4,5]
        usType5 = Combobox(P2, values=types, state="readonly",font=("arial", 10))
        usType5.set("Calificacion servicio")
        usType5.grid(row=8, column=1, padx=1, pady=1)
 
        
        print(usType5.get())
        boton = tk.Button(P2, text="Continuar")
        boton.grid(row=9, column=0, padx=1, pady=1)
        boton.bind("<Button-1>", verificar(huesped))
            
    
   
        