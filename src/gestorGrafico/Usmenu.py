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
from gestorAplicacion.usuarios.Empleado import Empleado
from gestorGrafico.FieldFrame import FieldFrame


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
        
        def volver():
            cls.menu(root, us)
        
        def isIni():                                            #logica para ver si ya se acabo o empezó la estadía
            fecha_actual = datetime.now()
            for hotel in Base.getHoteles():
                for habitacion in hotel.getHabitaciones():
                    if not habitacion.getReservada():
                        for reserv in habitacion.getReservas():
                            f_ini = reserv.getFechaEntrada().split("/")
                            fecha_ini = datetime(int(f_ini[2]), int(f_ini[1]), int(f_ini[0]))
                            if fecha_ini.date() == fecha_actual.date():
                                habitacion.setReservada(True)
                                huesped = reserv.getHuesped()
                                if huesped.getUsername() == us.getUsername():
                                    return True
            return False
        
        def isFin():
            fecha_actual = datetime.now()
            for hotel in Base.getHoteles():
                for habitacion in hotel.getHabitaciones():
                    if habitacion.getReservada():
                        for reserv in habitacion.getReservas():
                            f_fin = reserv.getFechaSalida().split("/")
                            fecha_fin = datetime(int(f_fin[2]), int(f_fin[1]), int(f_fin[0]))
                            
                            if fecha_actual.date() == fecha_fin.date():
                                habitacion.setReservada(False)
                                huesped = reserv.getHuesped()
                                if huesped.getUsername() == us.getUsername():
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
        
        
        
        if (isIni()):
                messagebox.showinfo("Empieza tu reserva", "Su Reserva ha comenzado, disfrute.")
                
        if (isFin()):
            us.setReserva(None)
            reserva = us.getReserva()
            costo = reserva.getCosto()
            messagebox.showinfo("Termina tu reserva", "Su Reserva ha terminado.\n\n"+
                                f"Costo total: {costo}") 
            
        
        prosCon.add_command(label="Reservar", command=reservar)             #Aquí se le agrega los commandos que llevan a las diferentes funcioanlidades
        
    
    
    
    
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

        if not cls.fTime:
            
            titulo = "Bienvenido " + us.getNombre()

            titulo = tk.Label(root, text=titulo, font=("Arial",20))
            titulo.pack(fill="both", pady=10)

            resumen = tk.Label(root, text="Escoge la opción que desear realizar.\nRecuerda que la funcionalidad de pagar empleados se encuentra en el menú en Procesos y consultas", font=("Arial",13))
            resumen.pack(pady=10)

            saldoHotel = Button(text="Ver saldo del hotel", command=verSaldoHotel)
            saldoHotel.pack(pady=10)
            registrarHabitacion = Button(text="Registrar nueva habitación")
            registrarHabitacion.pack(pady=10)
            cambiarSaldoHotel = Button(text="Cambiar el saldo del hotel")
            cambiarSaldoHotel.pack(pady=10)
            ultimoPago = Button(text="Ver la fecha del último pago")
            ultimoPago.pack(pady=10)
        
        
        def pagarEmpleados():
            def volver():
                cls.menu(root, us)

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
            saldoAPagar = us.saldoAPagarHotel(hotel.getEmpleados)
            respuesta3 = "El saldo que debe pagar el hotel es de: " + str(saldoAPagar)

            titulo1 = tk.Label(root, text=respuesta1, font=("Arial",20))
            titulo1.pack(fill="both", pady=10)

            titulo2 = tk.Label(root, text=respuesta2, font=("Arial",20))
            titulo2.pack(fill="both", pady=10)

            titulo3 = tk.Label(root, text=respuesta3, font=("Arial",20))
            titulo3.pack(fill="both", pady=10)

            pagar = Button(root, text="Pagar Empleados", command=pagar)
            pagar.pack(pady=10)

            

            volverPage = Button(root, text="Volver", command=volver)
            volverPage.pack(pady=10)


        prosCon.add_command(label="Pagar empleados", command=pagarEmpleados)   

        
    @classmethod
    def sistemaEmpleado(cls, root, us, prosCon):
        pass