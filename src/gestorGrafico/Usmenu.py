from datetime import datetime, date
import sys
from tkinter import Button, Menu, messagebox
import tkinter as tk
from tkinter.ttk import Combobox
from gestorGrafico import Root
from baseDatos.Base import Base
from gestorAplicacion.usuarios.Preferencia import Preferencia
from gestorAplicacion.usuarios.Huesped import Huesped
from gestorAplicacion.finanzas.CuentaBancaria import CuentaBancaria
from gestorAplicacion.hotel.Hotel import Hotel
from gestorAplicacion.hotel.Habitacion import Habitacion
from gestorAplicacion.hotel.TipoHabitacion import TipoHabitacion
from gestorAplicacion.finanzas.CuentaBancaria import CuentaBancaria
from gestorAplicacion.usuarios.Administrador import Administrador
from gestorAplicacion.hotel.ServiciosExtra import ServiciosExtra
from gestorAplicacion.usuarios.Empleado import Empleado
from gestorGrafico.FieldFrame import FieldFrame
from gestorGrafico.Calificar import Calificar
from errores.ErrorValores import ErrorValores


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
        
        
        root.cleanRoot()
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
        from gestorGrafico.Reservar import Reservar
        from gestorGrafico.Recomendaciones import Recomendaciones
        def volver():
            cls.menu(root, us)
        
        def isIni():                                            #logica para ver si ya se acabo o empezó la estadía
            fecha_actual = datetime.now().date()
            for hotel in Base.getHoteles():
                habs = hotel.getHabitaciones()
                for habitacion in habs:
                    res = habitacion.getReservada()
                    if not res:
                        reservs = habitacion.getReservas()
                        for reserv in reservs:
                            f_ini = reserv.getFechaEntrada().split("/")
                            fecha_ini = datetime(int(f_ini[2]), int(f_ini[1]), int(f_ini[0])).date()
                            if fecha_ini == fecha_actual:
                                huesped = reserv.getHuesped()
                                plantUser = huesped.getUsername()
                                oriUser = us.getUsername()
                                if plantUser == oriUser:
                                    habitacion.setReservada(True)
                                    return True
                                    
                                
            return False
        
        def isFin():
            fecha_actual = datetime.now().date()
            for hotel in Base.getHoteles():
                habs = hotel.getHabitaciones()
                for habitacion in habs:
                    res = habitacion.getReservada() 
                    if res:
                        reservs = habitacion.getReservas()
                        for reserv in reservs:
                            f_fin = reserv.getFechaSalida().split("/")
                            fecha_fin = datetime(int(f_fin[2]), int(f_fin[1]), int(f_fin[0])).date()
                            
                            if fecha_actual == fecha_fin:
                                huesped = reserv.getHuesped()
                                plantUser = huesped.getUsername()
                                oriUser = us.getUsername()
                                if plantUser == oriUser:
                                    habitacion.setReservada(False)
                                    return True
            return False
            
        
        def reservar():                             #Poner esto al inicio de cada funcionalidad (borra la información anterior)
            root.cleanRoot()
            root.title("CosmoReserve")
            menuBar = Menu(root)
            root.config(menu=menuBar)
            
            archivo = Menu(menuBar, tearoff=False)                              #opcion archivo 
            menuBar.add_cascade(label="Archivo", menu=archivo)
            archivo.add_command(label="Aplicación", command=root.aplicacion)
            archivo.add_command(label="Volver al menú", command=volver)
            archivo.add_command(label="Salir", command=root.salir)
            
            prosCon = Menu(menuBar, tearoff=False)                           #opcion procesos y consultas
            menuBar.add_cascade(label="Procesos y Consultas", menu=prosCon)
            
            ayuda = Menu(menuBar, tearoff=False)                           #opcion ayuda
            menuBar.add_cascade(label="Ayuda", menu=ayuda)
            ayuda.add_command(label="Acerca de", command=root.ayuda)
            prosCon.add_command(label="Reservar", command=reservar)
            
            Reservar.reservar(us, root, archivo)

        #RECOMENDACIONES

        def recomendacionesMenu():
            root.cleanRoot()
            root.title("CosmoReserve")
            menuBar = Menu(root)
            root.config(menu=menuBar)
            
            archivo = Menu(menuBar, tearoff=False)                          
            menuBar.add_cascade(label="Archivo", menu=archivo)
            archivo.add_command(label="Aplicación", command=root.aplicacion)
            archivo.add_command(label="Volver al menú", command=volver)
            archivo.add_command(label="Salir", command=root.salir)
            
            prosCon = Menu(menuBar, tearoff=False)                           
            menuBar.add_cascade(label="Procesos y Consultas", menu=prosCon)
            
            ayuda = Menu(menuBar, tearoff=False)                           
            menuBar.add_cascade(label="Ayuda", menu=ayuda)
            ayuda.add_command(label="Acerca de", command=root.ayuda)
            prosCon.add_command(label="Rcomendaciones", command=recomendacionesMenu)
            recomendaciones = Recomendaciones(us,root)
            recomendaciones.inicio()

        #AGREGAR_PREFERENCIA
        def agregarPreferencia():
            root.cleanRoot()
            root.title("CosmoReserve")
            menuBar = Menu(root)
            root.config(menu=menuBar)
            
            archivo = Menu(menuBar, tearoff=False)                          
            menuBar.add_cascade(label="Archivo", menu=archivo)
            archivo.add_command(label="Aplicación", command=root.aplicacion)
            archivo.add_command(label="Volver al menú", command=volver)
            archivo.add_command(label="Salir", command=root.salir)
            
            prosCon = Menu(menuBar, tearoff=False)                           
            menuBar.add_cascade(label="Procesos y Consultas", menu=prosCon)
            
            ayuda = Menu(menuBar, tearoff=False)                           
            menuBar.add_cascade(label="Ayuda", menu=ayuda)
            ayuda.add_command(label="Acerca de", command=root.ayuda)
            prosCon.add_command(label="Agregar preferencia", command=agregarPreferencia)
            recomendaciones = Recomendaciones(us,root)
            recomendaciones.agregarPreferencia()
            
        def verReserva():
            res = us.getReserva()
            if res != None:

                 

                hot = res.getHotel()
                hotel = hot.getNombre()
                city = hot.getCiudad()
                fechaIni = res.getFechaEntrada()
                fechaFin = res.getFechaSalida()
                cobroHabitacion = res.getCosto()
                textFin = ("Información:\n\n"+
                            f"Hotel: {hotel}\n\n"+
                            f"Ciudad: {city}\n\n"+
                            f"Fecha de inicio: {fechaIni}\n\n"+
                            f"Fecha de fin: {fechaFin}\n\n"+
                            f"Costo total: {cobroHabitacion}")
                messagebox.showinfo("Reserva", textFin)
            else:
                messagebox.showerror("Error", "No tiene reservas.")
                
        def verCB():
            def enviarSaldo():
                enviesaldo = deposito.get()
                if enviesaldo != "" or enviesaldo != "Saldo a depositar":
                    try:
                        enviSaldo = int(deposito.get())
                        CB.depositar(enviSaldo)
                        popup.destroy()
                        newSaldo = CB.getSaldo()
                        messagebox.showinfo("Exito", f"Has agregado correctamente {enviesaldo}$ a tu cuenta: {newSaldo}$")
                    except ValueError:
                        print("Error: No se pudo convertir el string a entero")
                        er = ErrorValores(deposito.widget_name, "Entero")
                        text = er.mostrarMensaje()
                        messagebox.showerror("Error", text)
                        popup.destroy()
                else:
                    popup.destroy()
            
            CB = us.getCuentaBancaria()
            saldo = CB.getSaldo()
            popup = tk.Toplevel(root)
            popup.title("Cuenta Bancaria")
            sal = tk.Label(popup, text=f"Saldo: ")
            sal.grid(row=0,column=0, pady=8, padx=3)
            money = tk.Label(popup, text=f"{saldo}")
            money.grid(row=0,column=1, pady=8, padx=3)
            an = tk.Label(popup, text="Depostiar dinero")
            an.grid(row=1, column=0, pady=8, padx=3)
            deposito = tk.Entry(popup)
            deposito.insert(0, "Saldo a depositar")
            deposito.widget_name = "saldo"
            deposito.grid(row=1, column=1, pady=8, padx=3)
            acept = tk.Button(popup, text="Enviar", command=enviarSaldo)
            acept.grid(row=2, column=0, pady=8, padx=3)
            
        
        if (isIni()):
                messagebox.showinfo("Empieza tu reserva", "Su Reserva ha comenzado, disfrute.")
                
        if (isFin()):
            reserva = us.getReserva()
            costo = reserva.getCosto()
            messagebox.showinfo("Termina tu reserva", "Su Reserva ha terminado.\n\n"+
                                f"Costo total: {costo}") 
            Calificar.seleccionar(root,us)
            #us.setReserva(None)

        #
        #Agregar servicio
        #

        def agregarServicio():

            res = us.getReserva()
            if res != None:

                def volver():
                    cls.menu(root, us)

                def crearServicio():

                    


                    def volver():
                        cls.menu(root, us)

                    tipo = combo.get()
                    tipo = tipo.split()

                    try:

                        tipo = tipo[0]

                    #tipoPrueba = combo.get()

                    except:

                        messagebox.showerror("Error", "Escoga un servicio")
                    
                    else:
                    
                        if tipo == "Transporte":

                            saldo = us.getCuentaBancaria().getSaldo()
                            valor = 2000

                            if saldo < valor:

                                messagebox.showerror("Error", "No cuentas con el dinero suficiente para pagar el servicio extra")
                            
                            else:

                                ServiciosExtra.agregarServicioTransporte(us)
                                messagebox.showinfo("Servicio agregado", "El servicio se ha agregado correctamente. El valor del servicio se ha descontado de su cuenta bancaria.")

                        elif tipo == "Alimentación":
                            
                            saldo = us.getCuentaBancaria().getSaldo()
                            valor = 1000

                            if saldo < valor:

                                messagebox.showerror("Error", "No cuentas con el dinero suficiente para pagar el servicio extra")
                                
                            
                            else:

                                ServiciosExtra.agregarServicioAlimentacion(us)
                                messagebox.showinfo("Servicio agregado", "El servicio se ha agregado correctamente. El valor del servicio se ha descontado de su cuenta bancaria.")




                        elif tipo == "Limpieza":
                            
                            saldo = us.getCuentaBancaria().getSaldo()
                            valor = 3000

                            if saldo < valor:

                                messagebox.showerror("Error", "No cuentas con el dinero suficiente para pagar el servicio extra")
                            
                            else:

                                ServiciosExtra.agregarServicioLimpieza(us)
                                messagebox.showinfo("Servicio agregado", "El servicio se ha agregado correctamente. El valor del servicio se ha descontado de su cuenta bancaria.")


                        volver()

                root.cleanRoot()
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

                prosCon.add_command(label="Ver reserva", command=verReserva)
                prosCon.add_command(label="Ver Cuenta Bancaria", command=verCB)
                prosCon.add_command(label="Recomendaciones",command=recomendacionesMenu)          #Aquí se le agrega los commandos que llevan a las diferentes funcioanlidades
                prosCon.add_command(label="Agregar preferencia",command=agregarPreferencia) 
            
                prosCon.add_command(label="Agregar servicio", command=agregarServicio) 
                prosCon.add_command(label="Quitar servicio", command=quitarServicio) 

                titulo = tk.Label(root, text="Agregar servicio", font=("Arial",20))
                titulo.pack(fill="both", pady=10)

                servicios = ServiciosExtra.listServiciosExtra(us)

                if not (servicios == False):
                    
                    desc = tk.Label(root, text="Actualmente cuentas con los siguientes servicios", font=("Arial",13))
                    desc.pack(fill="both", pady=10)

                    for i in servicios:

                        salida = "- " + str(i.getTipoServicio())
                        serv = tk.Label(root, text=salida, font=("Arial",13))
                        serv.pack(fill="both", pady=10)



                desc2 = tk.Label(root, text="Escoga el servicio que desea agregar", font=("Arial",13))
                desc2.pack(fill="both", pady=10)

                combo =  Combobox(root, values=["Transporte $2000", "Alimentación $1000", "Limpieza $3000"])
                combo.pack(pady=10)

                asignarbtn = Button(root, text="Agregar", command=crearServicio)
                asignarbtn.pack(pady=10)

                volver1 = Button(root, text="Volver", command=volver)
                volver1.pack(pady=10)

            else:
                messagebox.showerror("Error", "Para acceder a un servicio extra necesitas de una reserva")
                            





        def quitarServicio():

            res = us.getReserva()
            if res != None:

                def volver():
                    cls.menu(root, us)

                def quitarServicioExtra():

                    def volver():
                        cls.menu(root, us)
                
                    servicios = ServiciosExtra.listServiciosExtra(us)
                    tipo = combo.get()
                    

                    if tipo == None or tipo == "":
                        messagebox.showerror("Error", "Debe escoger el servicio extra a eliminar")

                    else:

                        tipoList = tipo.split()
                        tipoIndex = int(tipoList[0]) - 1

                        ServiciosExtra.eliminarServicio(us, servicios[tipoIndex])
                        messagebox.showinfo("Servicio eliminado", "El servicio se ha eliminado correctamente. Se ha devuelto el dinero a tu cuenta")

                        volver()


                root.cleanRoot()
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

                prosCon.add_command(label="Ver reserva", command=verReserva)
                prosCon.add_command(label="Ver Cuenta Bancaria", command=verCB)
                prosCon.add_command(label="Recomendaciones",command=recomendacionesMenu)          #Aquí se le agrega los commandos que llevan a las diferentes funcioanlidades
                prosCon.add_command(label="Agregar preferencia",command=agregarPreferencia) 
            
                prosCon.add_command(label="Agregar servicio", command=agregarServicio) 
                prosCon.add_command(label="Quitar servicio", command=quitarServicio) 

                titulo = tk.Label(root, text="Quitar servicio", font=("Arial",20))
                titulo.pack(fill="both", pady=10)

                servicios = ServiciosExtra.listServiciosExtra(us)

                serviciosCombo = []

                if not (servicios == False):
                    
                    desc = tk.Label(root, text="Actualmente cuentas con los siguientes servicios", font=("Arial",13))
                    desc.pack(fill="both", pady=10)

                    contador = 1

                    for i in servicios:

                        salida = "- " + str(i.getTipoServicio())
                        serv = tk.Label(root, text=salida, font=("Arial",13))
                        serv.pack(fill="both", pady=10)

                        serviciosCombo.append(str(contador) + " " + i.getTipoServicio())
                        contador += 1


                    desc2 = tk.Label(root, text="Escoga el servicio que desea eliminar", font=("Arial",13))
                    desc2.pack(fill="both", pady=10)

                    combo =  Combobox(root, values=serviciosCombo)
                    combo.pack(pady=10)

                    asignarbtn = Button(root, text="Eliminar", command=quitarServicioExtra)
                    asignarbtn.pack(pady=10)
                
                else:

                    messagebox.showinfo("Servicio agregado", "Actualmente no cuentas con Servicios extra")

                    volver()


                volver1 = Button(root, text="Volver", command=volver)
                volver1.pack(pady=10)

            else:
                messagebox.showerror("Error", "Para acceder a un servicio extra necesitas de una reserva")
            
        
        prosCon.add_command(label="Reservar", command=reservar)             #Aquí se le agrega los commandos que llevan a las diferentes funcioanlidades
        #prosCon.add_command(label="calificar", command=Calificar.seleccionar(root,us))
        prosCon.add_command(label="Ver reserva", command=verReserva)
        prosCon.add_command(label="Ver Cuenta Bancaria", command=verCB)
        prosCon.add_command(label="Recomendaciones",command=recomendacionesMenu)          #Aquí se le agrega los commandos que llevan a las diferentes funcioanlidades
        prosCon.add_command(label="Agregar preferencia",command=agregarPreferencia) 
    
        prosCon.add_command(label="Agregar servicio", command=agregarServicio) 
        prosCon.add_command(label="Quitar servicio", command=quitarServicio) 
    
    
    
    @classmethod
    def sistemaAdministrador(cls, root, us, prosCon):

        ##############################################
        #       Información pre-cargada  
        ##############################################

        # cuentaBancariaH = CuentaBancaria(1000000, "b")
        # cuentaBancariaA = CuentaBancaria(1000000, "b")
        # cuentaBancariaE1 = CuentaBancaria(1000000, "b")
        # cuentaBancariaE2 = CuentaBancaria(1000000, "b")

        # habitaciones = []
        # hab1 = Habitacion(1, "simple", TipoHabitacion.asign_camas(TipoHabitacion.SIMPLE), TipoHabitacion.asign_precio(TipoHabitacion.SIMPLE))
        # hab1.addCalificacion(Huesped(), 3)
        # hab1.addCalificacion(Huesped(), 2)
        # hab2 = Habitacion(2, "doble", TipoHabitacion.asign_camas(TipoHabitacion.DOBLE), TipoHabitacion.asign_precio(TipoHabitacion.DOBLE))
        # hab2.addCalificacion(Huesped(), 3)
        # hab2.addCalificacion(Huesped(), 3)

        # habitaciones.append(hab1)
        # habitaciones.append(hab2)

        # hotel = Hotel(cuentaBancariaH, "Hotel1", "Medellín", [], habitaciones, [])

        # administrador1 = Administrador("Camilo", 12345, "kmi", "12345", cuentaBancariaA, hotel)

        # empleado1 = Empleado("Juan", 12344, "juanjo", "12345", cuentaBancariaE1, hotel, True, 3000)
        # empleado2 = Empleado("Carlos", 12333, "calitos", "12345", cuentaBancariaE2, hotel, True, 300)

        # Base.addHoteles(hotel)
        # Base.addAdministradores(administrador1)
        # Base.addEmpleados(empleado1)
        # Base.addEmpleados(empleado2)



        ##############################################

        #
        #Ver saldo del hotel
        #

        def verSaldoHotel():

            def volver():
                cls.menu(root, us)

            root.cleanRoot()
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

            hotel = us.getHotel()
            saldo = hotel.getCuentaBancaria().getSaldo()
            respuesta = "El hotel " + us.getHotel().getNombre() + " tiene un saldo de " + str(saldo)

            titulo = tk.Label(root, text=respuesta, font=("Arial",20))
            titulo.pack(fill="both", pady=10)

            volver = Button(root, text="Volver", command=volver)
            volver.pack(pady=10)


        #
        #Listar habitaciones
        #

        def mostrarHabitaciones():

            def volver():
                cls.menu(root, us)

            root.cleanRoot()
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

            respuesta = "Lista de habitaciones en el hotel" + us.getHotel().getNombre()
            hotel = us.getHotel()
            habitaciones = hotel.getHabitaciones()

            titulo = tk.Label(root, text=respuesta, font=("Arial",20))
            titulo.pack(fill="both", pady=10)
            
            num = 1
            for i in habitaciones:
                text = str(num) + ". " + i.getTipo()
                habitacion = tk.Label(root, text=text, font=("Arial",13))
                habitacion.pack(fill="both", pady=10)

                num += 1

            volverS = Button(root, text="Volver", command=volver)
            volverS.pack(pady=10)


        #
        #Registrar nueva habitación
        #

        def regisHabitacion():

            def volver():
                cls.menu(root, us)

            #
            #Se crea el nuevo objeto habitación
            #
            def crearHabitacion():

                def volver():
                    cls.menu(root, us)

                tip = combo.get()
                tipo = combo.get().split()

                if tip == "" or tip == None:

                    messagebox.showerror("Error", "Por favor escoga el tipo de habitación para poder registrarla en el hotel")
    
                elif tipo[0] in "FAMILIAR":

                    habitacion = Habitacion(19, "Familiar", TipoHabitacion.asign_camas(TipoHabitacion.FAMILIAR), TipoHabitacion.asign_precio(TipoHabitacion.FAMILIAR))

                elif tipo[0] in "DOBLE":

                    habitacion = Habitacion(19, "Doble", TipoHabitacion.asign_camas(TipoHabitacion.DOBLE), TipoHabitacion.asign_precio(TipoHabitacion.DOBLE))

                elif tipo[0] in "SIMPLE":

                    habitacion = Habitacion(19, "Simple", TipoHabitacion.asign_camas(TipoHabitacion.SIMPLE), TipoHabitacion.asign_precio(TipoHabitacion.SIMPLE))

                elif tipo[0] in "VIPFAMILIAR":

                    habitacion = Habitacion(19, "VIPFamiliar", TipoHabitacion.asign_camas(TipoHabitacion.VIPFAMILIAR), TipoHabitacion.asign_precio(TipoHabitacion.VIPFAMILIAR))

                elif tipo[0] in "VIPDOBLE":

                    habitacion = Habitacion(19, "VIPDoble", TipoHabitacion.asign_camas(TipoHabitacion.VIPDOBLE), TipoHabitacion.asign_precio(TipoHabitacion.VIPDOBLE))

                elif tipo[0] in "VIPSIMPLE":

                    habitacion = Habitacion(19, "VIPSimple", TipoHabitacion.asign_camas(TipoHabitacion.VIPSIMPLE), TipoHabitacion.asign_precio(TipoHabitacion.VIPSIMPLE))

                try:

                    us.getHotel().addHabitacion(habitacion)

                except UnboundLocalError:
                    print("Debe escoger una habitación para poder registrarla")
                    messagebox.showerror("Error", "Escoga un tipo de habitación")


                else:
                    messagebox.showinfo("Operación Completa", "La habitación se ha registrado correctamente")
                    volver()

            root.cleanRoot()
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

            

            titulo = tk.Label(root, text="Registrar nueva habitación", font=("Arial",20))
            titulo.pack(fill="both", pady=10)

            respuesta = "Hotel al cual se le va a registrar la habitación: " + us.getHotel().getNombre()

            titulo = tk.Label(root, text=respuesta, font=("Arial",13))
            titulo.pack(fill="both", pady=10)

            texto = tk.Label(root, text="Escoge el tipo de habitación que deseas registrar", font=("Arial",13))
            texto.pack(fill="both", pady=10)

            tipoDefecto = tk.StringVar(root, value = "Tipo de Habitación")

            tiposHabitacion = []

            for i in TipoHabitacion:
                habitacion = str(i.name) + " (" + str(i.value[0]) + " camas)"
                tiposHabitacion.append(habitacion)


            combo =  Combobox(root, values=tiposHabitacion, textvariable=tipoDefecto)
            combo.pack(pady=10)

            asignarbtn = Button(root, text="Registrar", command=crearHabitacion)
            asignarbtn.pack(pady=10)

            volver = Button(root, text="Volver", command=volver)
            volver.pack(pady=10)

        #
        #Cambiar el saldo del hotel
        #

        def cambiarSaldoHot():

            def cambiar():

                entrada = entry.get()

                if(entrada == "" or entrada == None):

                    messagebox.showerror("Error", "Por favor escoga el valor para cambiar el saldo del hotel")

                try:
                    valor_entero = int(entrada)
        
                except ValueError:

                    messagebox.showerror("Error", "Ingrese un valor entero válido")
            
                else:

                    us.getHotel().getCuentaBancaria().setSaldo(valor_entero)

                    messagebox.showinfo("Operación Completa", "La habitación se ha cambiado el saldo del hotel correctamente")
                    volver()
            
            def volver():
                cls.menu(root, us)

            root.cleanRoot()
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

            titulo = tk.Label(root, text="Cambiar el saldo del Hotel", font=("Arial",20))
            titulo.pack(fill="both", pady=10)

            hotel = us.getHotel()
            saldo = hotel.getCuentaBancaria().getSaldo()
            respuesta = "El hotel " + us.getHotel().getNombre() + " tiene un saldo de " + str(saldo)

            titulo = tk.Label(root, text=respuesta, font=("Arial",15))
            titulo.pack(fill="both", pady=10)

            frame = tk.Frame(root, width=200, height=100)

            labelSaldo = tk.Label(frame, text="Nuevo saldo: ", font=("Arial",13))
            entry = tk.Entry(frame)

            labelSaldo.grid(row = 0, column=0, sticky="w")
            entry.grid(row=0, column=1)

            frame.pack(pady=10)

            cambiar = Button(root, text="Cambiar", command=cambiar)
            cambiar.pack(pady=10)

            volvera = Button(root, text="Volver", command=volver)
            volvera.pack(pady=10)


        #
        #Fecha de último pago
        #

        def fechUltimoPag():

            def volver():
                cls.menu(root, us)

            root.cleanRoot()
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

            fecha = str(us.getUltimoPago())

            titulo = tk.Label(root, text="Ultimo Pago", font=("Arial",20))
            titulo.pack(fill="both", pady=10)

            ultimoP = "El último pago se realizó el " + fecha

            titulo = tk.Label(root, text=ultimoP, font=("Arial",20))
            titulo.pack(pady=10)

            #
            #Borrar último pago
            #

        
            def delteUltimoPago():
                
                us.reiniciarUltimoPago()
                messagebox.showinfo("Operación Completa", "Se reinició la última fecha del pago completamente")
                volver()


            reiniciarUlp = Button(root, text="Reiniciar Fecha", command=delteUltimoPago)
            reiniciarUlp.pack(pady=10)

            volvera = Button(root, text="Volver", command=volver)
            volvera.pack(pady=10)

        


        #
        #Administrador después del login
        #

        if not cls.fTime:
            
            titulo = "Bienvenido " + us.getNombre()

            saldoAdmin = "Tienes un saldo de: " + str(us.getCuentaBancaria().getSaldo())

            titulo = tk.Label(root, text=titulo, font=("Arial",20))
            titulo.pack(fill="both", pady=10)

            descrop = tk.Label(root, text=saldoAdmin, font=("Arial",15))
            descrop.pack(fill="both", pady=10)

            resumen = tk.Label(root, text="Escoge la opción que desear realizar.\nRecuerda que la funcionalidad de pagar empleados se encuentra en el menú en Procesos y consultas", font=("Arial",13))
            resumen.pack(pady=10)

            saldoHotel = Button(text="Ver saldo del hotel", command=verSaldoHotel)
            saldoHotel.pack(pady=10)
            listHabitaciones = Button(text="Listar habitaciones", command=mostrarHabitaciones)
            listHabitaciones.pack(pady=10)
            registrarHabitacion = Button(text="Registrar nueva habitación", command=regisHabitacion)
            registrarHabitacion.pack(pady=10)
            cambiarSaldoHotel = Button(text="Cambiar el saldo del hotel", command=cambiarSaldoHot)
            cambiarSaldoHotel.pack(pady=10)
            ultimoPago = Button(text="Ver la fecha del último pago", command=fechUltimoPag)
            ultimoPago.pack(pady=10)

        #
        # Funcionalidada para pagar empleados
        #
        
        
        def pagarEmpleados():
            def volver():
                cls.menu(root, us)

            #
            #Pagar a los empleados - messagebox
            #

            def pagar():

                resultado = us.pagarEmpleados()

                if resultado == 1:

                    messagebox.showerror("Error", "No se pudo realizar el pago ya que no han pasado más de 30 días desde el último pago")

                elif resultado == 2:

                    messagebox.showerror("Error", "No se pudo realizar el pago ya que el hotel no tiene el saldo suficiente")

                elif resultado == 0:

                    messagebox.showinfo("Funcionalidad Completa", "El pago se ha realizado correctamente")
                    volver()

            root.cleanRoot()
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

            hotel = us.getHotel()
            saldo = hotel.getCuentaBancaria().getSaldo()
            respuesta1 = "El hotel " + us.getHotel().getNombre() + " tiene un saldo de: " + str(saldo)

            if us.getUltimoPago() != None:

                ultimoPago = us.getUltimoPago()

            else:

                ultimoPago = "No se han realizados pagos"

            respuesta2 = "El último pago se realizó el: " + str(ultimoPago)
            saldoAPagar = us.saldoAPagarHotel(hotel.getEmpleados())
            respuesta3 = "El saldo que debe pagar el hotel es de: " + str(saldoAPagar)

            titulo1 = tk.Label(root, text="Funcionalidad Pagar Empleados", font=("Arial",20))
            titulo1.pack(fill="both", pady=10)

            titulo1 = tk.Label(root, text=respuesta1, font=("Arial",15))
            titulo1.pack(fill="both", pady=10)

            titulo2 = tk.Label(root, text=respuesta2, font=("Arial",15))
            titulo2.pack(fill="both", pady=10)

            titulo3 = tk.Label(root, text=respuesta3, font=("Arial",15))
            titulo3.pack(fill="both", pady=10)

            descripcionP = tk.Label(root, text="La funcionalidad de pagar empleados le permite a el administrador hacer el respectivo pago a los empleados.\n Se le descuenta el dinero a la cuenta bancaria del hotel.\nLos pagos se hacen minimo cada mes ", font=("Arial",13))
            descripcionP.pack(fill="both", pady=10)

            pagar = Button(root, text="Pagar Empleados", command=pagar)
            pagar.pack(pady=10)

            

            volverPage = Button(root, text="Volver", command=volver)
            volverPage.pack(pady=10)

        #
        #Agregar la funcionalidad al menú
        #


        prosCon.add_command(label="Pagar empleados", command=pagarEmpleados)   

        
    @classmethod
    def sistemaEmpleado(cls, root, us, prosCon):
        pass