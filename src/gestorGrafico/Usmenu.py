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
from gestorGrafico.FieldFrame import FieldFrame
from gestorGrafico.Reservar import Reservar

#@autor: David Restrepo

class Usmenu():
    
    fTime = False
    pl = None
    pr = None
    
    @classmethod
    def menu(cls, root:Root, us, fTime=False):              
        
        def firstTime(us):                                     #Información en caso de primera vez
            cls.fTime = True
            cls.pl = tk.Frame(root)
            cls.pl.place(relwidth=0.4, relheight=1, relx=0.003, rely=0, anchor="nw")
            tituloResumen = tk.Label(cls.pl, text="Resumen", font=("Arial",20))
            tituloResumen.pack(fill="both", pady=10)
            txt1 = tk.Text(cls.pl)
            
            txt1.insert(tk.END, "CosmoReserve es un programa diseñado para gestionar una cadena de hotelería." +
                                    "Esteprograma consta de diferentes funcionalidades de acuerdo al tipo " +
                                    "de usuario, ya sea un cliente o un administrador. Estos tendrán que registrarse" +
                                    "e iniciar sesión para acceder a dichas funcionalidades." +
                                    "\n\nPor un lado, el administrador podrá crear hoteles, sus" +
                                    "respectivas habitaciones yservicios; también, administrar todo lo que corresponde" +
                                    "a los servicios y las finanzas de los hoteles. Por otro lado, los clientes, tanto VIP" +
                                    "como normales, pueden reservar habitaciones en un hotel específico, asistir a los" +
                                    "diferentes servicios de dicho hotel, obtener descuentos al momento de reservar y recibir" +
                                    "recomendaciones de acuerdo a sus experiencias y gustos. Los clientes VIP pueden reservar" +
                                    "habitaciones especiales que los clientes normales no podrán.")
            
            txt1.configure(state="disable")
            txt1.pack(fill="both", pady=10)
            
            
            cls.pr = tk.Frame(root)
            cls.pr.place(relwidth=0.4, relheight=1, relx=0.997, rely=0, anchor="ne")
            tituloFuncionalidad = tk.Label(cls.pr, text="Funcionalidades", font=("Arial",20))
            tituloFuncionalidad.pack(fill="both", pady=10)
            txt2 = tk.Text(cls.pr)
            
            if (us == "huesped"):
                txt2.insert(tk.END, "Reservar: tiene la posibilidad de buscar la habitación en la que se hospedará, "+ 
                                    "primero buscando el hotel que desea y luego la habitación. \n\n"+
                                    "Recomendaciones: tendrá la posibilidad de ver las recomendaciones de "+
                                    "hoteles y habitaciones que tiene la cadena hotelera para él, ya sea basadas " +
                                    "en su experiencia o en la experiencia de otros clientes que cumplan con su perfil.\n\n"+
                                    "Calificaciones: el usuario tendrá que calificar la habitación en la que se hospedó, así"+ 
                                    "mismo en caso de haber adquirido algún servicio extra y/o relacionado con algún empleado.")
            
                txt2.configure(state="disable")
                txt2.pack(fill="both", pady=10)
                
            elif (us == "administrador"):
                txt2.insert(tk.END, "Servicios: el administrador tiene la posibilidad de dar un servicio al cliente según sus "+
                                    "parámetros y lo que fuese solicitado.\n\n"+
                                    "Pago por administrador: El usuario administrador podrá depositar el respectivo sueldo de cada "+
                                    "empleado desde la cuenta del hotel, hasta las cuentas de cada empleado. Solo se puede depositar "+
                                    "a los empleados una vez por mes.\n\n")
            
                txt2.configure(state="disable")
                txt2.pack(fill="both", pady=10)
                
            else:
                txt2.insert(tk.END, "Pago por administrador: El administrador podrá depositar el respectivo sueldo " +
                                    "de cada empleado.")
            
                txt2.configure(state="disable")
                txt2.pack(fill="both", pady=10)
        
        
        
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
            if fTime : firstTime("huesped")                 #Revisar si es primera vez entrando, entonces mostrar el resumen de la aplicación
        elif isinstance(us, Administrador):
            cls.sistemaAdministrador(root, us, prosCon)
            if fTime : firstTime("administrador")
        else:
            cls.sistemaEmpleado(root, us, prosCon)
            if fTime : firstTime("empleado")
            
    @classmethod
    def sistemaHuesped(cls, root, us, prosCon):
        def reservar():                             #Poner esto al inicio de cada funcionalidad (borra la información anterior)
            if cls.fTime:
                cls.pl.destroy()
                cls.pr.destroy()
            
            
            
            Reservar.reservar(us, root)
                
                        
            # criterios = ["nombre", "contra", "hola"]                  //Prueba FieldFrame
            # vals = ["str", "str", "int"]
            # desabilitados = ["contra"]
            # p1 = tk.Frame(root, background="white")
            # p1.pack(expand=True, fill="both")
            # form = FieldFrame("cri", criterios, "vals", vals, desabilitados)
            # form.setRoot(p1)
            # form.getFrame().place(anchor="center", relx=0.5, rely=0.5)
            
            
        prosCon.add_command(label="Reservar", command=reservar)             #Aquí se le agrega los commandos que llevan a las diferentes funcioanlidades
        
    
    
    
    
    @classmethod
    def sistemaAdministrador(cls, root, us, prosCon):
        pass
        
    @classmethod
    def sistemaEmpleado(cls, root, us, prosCon):
        pass