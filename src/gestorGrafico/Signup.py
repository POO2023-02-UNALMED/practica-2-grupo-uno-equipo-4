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

#@autor: David Restrepo

class Signup():
    nombre_entry = object
    telefono_entry = object
    username_entry = object
    password_entry = object
    
    @classmethod
    def iniciar(cls, root:Root):
        
        def continuar(event):
            if (usType.get() == "Huesped"):
                P2.destroy()
                cls.registroHuesped(P1, root)
            elif usType.get() == "Administrador":
                root.cleanRoot()
                cls.registroAdministrador(root)
            else:
                root.cleanRoot()
                cls.registroEmpleado(root)
                #print("No puede registrarse por sí solo, esto lo tiene que hacer el administrador")
        
        
        root.title("SignUp")
        
        menuBar = Menu(root)
        root.config(menu=menuBar)
        archivo = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Archivo", menu=archivo)
        archivo.add_command(label="Salir", command=root.salir)
        
        signLabel = tk.Label(root, text="Registrarse", font=("arial", 30))
        signLabel.pack(side="top", padx=10, pady=10,)
        
        #Seleccionar que tipo de usuario es
        P1 = tk.Frame(root, bg="red")
        P1.pack(side="top", fill="both", expand=True)
        P2 = tk.Frame(P1, bg="yellow")
        P2.place(relx=0.5, rely=0.1, relheight=0.15, anchor="c")
        # P2.pack(anchor="c", pady=10, fill="y")
        typesLabel = tk.Label(P2, text="Tipo de usuario:")
        typesLabel.grid(row=0, column=0, padx=1, pady=1)
        types = ["Huesped", "Administrador", "Empleado"]
        usType = Combobox(P2, values=types, state="readonly",font=("arial", 10))
        usType.set("Tipo de usuario")
        usType.grid(row=0, column=1, padx=1, pady=1)
                
        
        
        
        cont = tk.Button(P2, text="Continuar")
        cont.place(y=60, relx=0.5, anchor="c")
        cont.bind("<Button-1>", continuar)
    
    
    #Registro huesped
    @classmethod
    def registroHuesped(cls, P1, root):
        global nombre_entry
        global telefono_entry
        global username_entry
        global password_entry
        def compareName(event):
            rNom = False
            username = username_entry.get()  # Obtener el valor del Entry en tkinter
            for x in Base.getHuespedes():
                if x.getUsername() == username:
                    print("\nEste nombre ya está en uso. Intente de nuevo\n")
                    rNom = True
                    break
            if rNom == False:
                cont_button.destroy()
                nombre_entry["state"] = "disable"
                password_entry["state"] = "disable"
                username_entry["state"] = "disable"
                telefono_entry["state"] = "disable"
                cls.continueRegistroHuesped(P3, root)
        
        P3 = tk.Frame(P1, bg="blue", pady=10)
        P3.place(relx=0.5 ,relheight=1, anchor="n")
        nombre_label = tk.Label(P3, text="Ingrese su nombre completo:")
        nombre_label.grid(row=0, column=0, padx=1, pady=1)
        nombre_entry = tk.Entry(P3)
        nombre_entry.grid(row=0, column=1, padx=1, pady=1)
        
        telefono_label = tk.Label(P3, text="Ingrese su número de teléfono:")
        telefono_label.grid(row=1, column=0, padx=1, pady=1)
        telefono_entry = tk.Entry(P3)
        telefono_entry.grid(row=1, column=1, padx=1, pady=1)
        
        username_label = tk.Label(P3, text="Ingrese un nombre de usuario:")
        username_label.grid(row=2, column=0, padx=1, pady=1)
        username_entry = tk.Entry(P3)
        username_entry.grid(row=2, column=1, padx=1, pady=1)
        
        password_label = tk.Label(P3, text="Ingrese una contraseña:")
        password_label.grid(row=3, column=0, padx=1, pady=1)
        password_entry = tk.Entry(P3, show="*")  # Use show="*" to hide the password
        password_entry.grid(row=3, column=1, padx=1, pady=1)
        
        cont_button = tk.Button(P3, text="Continuar")
        cont_button.place(rely=0.2, relx=0.5, anchor="c")
        cont_button.bind("<Button-1>", compareName)
        
    @classmethod
    def continueRegistroHuesped(cls, P3, root):
        
        def terminar(event):
            preferencias = []
            preferencia = Preferencia(city_combobox.get(), hotels_combobox.get(), habitaciones_combobox.get())
            preferencias.append(preferencia)
            huesped = Huesped (bool(is_vip_var), preferencias, nombre_entry.get(), telefono_entry.get(), username_entry.get(), password_entry.get(), CuentaBancaria(saldo_entry.get(), banco_entry.get()))
            Base.addHuespedes(huesped)
        
            if (is_bono_var):
                huesped.ofrecerBono()
            cls.intro(huesped)
            
            root.cleanRoot()
            Usmenu.menu(root, huesped)
        
        saldo_label = tk.Label(P3, text="Ingrese el saldo de su cuenta:")
        saldo_label.grid(column=0, row=4)

        saldo_entry = tk.Entry(P3)
        saldo_entry.grid(column=1, row=4)

        banco_label = tk.Label(P3, text="Ingrese el banco al que pertenece:")
        banco_label.grid(column=0, row=5)

        banco_entry = tk.Entry(P3)
        banco_entry.grid(column=1, row=5)

        
        is_vip_label = tk.Label(P3, text="¿Desea ser un huésped VIP?")
        is_vip_label.grid(column=0, row=6, padx=1, pady=1)

        is_vip_var = tk.BooleanVar()
        cajon = tk.LabelFrame(P3)
        is_vip_radiobutton1 = tk.Radiobutton(cajon, text="Sí", variable=is_vip_var, value=True)
        is_vip_radiobutton2 = tk.Radiobutton(cajon, text="No", variable=is_vip_var, value=False)
        cajon.grid(column=1, row=6, padx=1, pady=1)
        is_vip_radiobutton1.pack(side="left")
        is_vip_radiobutton2.pack(side="right")
        
        listaCiudades = []
        hoteles = Base.getHoteles()
        for x in hoteles:
            if x.getCiudad() not in listaCiudades:
                listaCiudades.append(x.getCiudad())
        
        cities_label = tk.Label(P3, text="Elija la ciudad de su preferencia:")
        cities_label.grid(column=0, row=7, padx=1, pady=1)

        city_combobox = Combobox(P3, values=listaCiudades, state="readonly")
        city_combobox.set("Ciudades")
        city_combobox.grid(column=1, row=7, padx=1, pady=1)
        
        
        listaNombres = []
        for x in hoteles:
            if x.getNombre() not in listaNombres:
                listaCiudades.append(x.getNombre())
        
        hotel_label = tk.Label(P3, text="Elija el hotel que prefiere en nuestra cadena:")
        hotel_label.grid(column=0, row=8, padx=1, pady=1)

        hotels_combobox = Combobox(P3, values=listaNombres, state="readonly")
        hotels_combobox.set("Hoteles")
        hotels_combobox.grid(column=1, row=8, padx=1, pady=1)
        
        
        listaHabitaciones = ["simple", "doble", "familiar", "vipsimple", "vipdoble", "vipfamiliar"]
        habitaciones_label = tk.Label(P3, text="Elija el tipo de habitación que prefiere de la siguiente lista:")
        habitaciones_label.grid(column=0, row=9, padx=1, pady=1)

        habitaciones_combobox = Combobox(P3, values=listaHabitaciones, state="readonly")
        habitaciones_combobox.set("Habitaciones")
        habitaciones_combobox.grid(column=1, row=9, padx=1, pady=1)
        
        
        
        is_bono_label = tk.Label(P3, text="¿Quiere que se le envíe publicidad?")
        is_bono_label.grid(column=0, row=10, padx=1, pady=1)

        is_bono_var = tk.BooleanVar()
        cajon = tk.LabelFrame(P3)
        is_bono_radiobutton1 = tk.Radiobutton(cajon, text="Sí", variable=is_bono_var, value=True)
        is_bono_radiobutton2 = tk.Radiobutton(cajon, text="No", variable=is_bono_var, value=False)
        cajon.grid(column=1, row=10, padx=1, pady=1)
        is_bono_radiobutton1.pack(side="left")
        is_bono_radiobutton2.pack(side="right")
        
        endRegist = tk.Button(P3, text="Enviar")
        endRegist.place(relx=0.5, rely=0.5, anchor="n")
        endRegist.bind("<Button-1>", terminar)
        
        
    @classmethod
    def intro(cls, us):
        print(us.presentacion())
        
        
    
    
    #Registro administrador
    @classmethod
    def registroAdministrador(cls, root:Root):
        
        global nombre_entry
        global telefono_entry
        global username_entry
        global password_entry
        def compareName(event):
            rNom = False
            username = username_entry.get()  # Obtener el valor del Entry en tkinter
            for x in Base.getAdministradores():
                if x.getUsername() == username:
                    print("\nEste nombre ya está en uso. Intente de nuevo\n")
                    rNom = True
                    break
            if rNom == False:
                cont_button.destroy()
                nombre_entry["state"] = "disable"
                password_entry["state"] = "disable"
                username_entry["state"] = "disable"
                telefono_entry["state"] = "disable"
                cls.continueRegistroAdministrador(P2, root)
        
        root.title("SignUp")
        
        menuBar = Menu(root)
        root.config(menu=menuBar)
        archivo = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Archivo", menu=archivo)
        archivo.add_command(label="Salir", command=root.salir)
        
        signLabel = tk.Label(root, text="Registrarse", font=("arial", 30))
        signLabel.pack(side="top", padx=10, pady=10,)
        
        P1 = tk.Frame(root, bg="red")
        P1.pack(side="top", fill="both", expand=True)
        
        P2 = tk.Frame(P1, bg="blue", pady=10)
        P2.place(relx=0.5 ,relheight=1, anchor="n")
        nombre_label = tk.Label(P2, text="Ingrese su nombre completo:")
        nombre_label.grid(row=0, column=0, padx=1, pady=1)
        nombre_entry = tk.Entry(P2)
        nombre_entry.grid(row=0, column=1, padx=1, pady=1)
        
        telefono_label = tk.Label(P2, text="Ingrese su número de teléfono:")
        telefono_label.grid(row=1, column=0, padx=1, pady=1)
        telefono_entry = tk.Entry(P2)
        telefono_entry.grid(row=1, column=1, padx=1, pady=1)
        
        username_label = tk.Label(P2, text="Ingrese un nombre de usuario:")
        username_label.grid(row=2, column=0, padx=1, pady=1)
        username_entry = tk.Entry(P2)
        username_entry.grid(row=2, column=1, padx=1, pady=1)
        
        password_label = tk.Label(P2, text="Ingrese una contraseña:")
        password_label.grid(row=3, column=0, padx=1, pady=1)
        password_entry = tk.Entry(P2, show="*")  # Use show="*" to hide the password
        password_entry.grid(row=3, column=1, padx=1, pady=1)
        
        cont_button = tk.Button(P2, text="Continuar")
        cont_button.place(rely=0.2, relx=0.5, anchor="c")
        cont_button.bind("<Button-1>", compareName)
        
    
    @classmethod
    def continueRegistroAdministrador(cls, P2, root):
        def terminar(event):
            hotel = None
            selectedHotel = hotel_combobox.get()
            for x in hoteles:
                if x.getNombre() == selectedHotel:
                    hotel = x
            administrador = Administrador(nombre_entry.get(), telefono_entry.get(), username_entry.get(), password_entry.get(), CuentaBancaria(saldo_entry.get(), banco_entry.get()), hotel)
            Base.addAdministradores(administrador)
            
            root.cleanRoot()
            Usmenu.menu(root, administrador)

        
        saldo_label = tk.Label(P2, text="Ingrese el saldo de su cuenta:")
        saldo_label.grid(column=0, row=4)

        saldo_entry = tk.Entry(P2)
        saldo_entry.grid(column=1, row=4)

        banco_label = tk.Label(P2, text="Ingrese el banco al que pertenece:")
        banco_label.grid(column=0, row=5)

        banco_entry = tk.Entry(P2)
        banco_entry.grid(column=1, row=5)
        
        listaNombres = []
        hoteles = Base.getHoteles()
        for x in hoteles:
            if x.getNombre() not in listaNombres:
                listaNombres.append(x.getNombre())
        
        hotel_label = tk.Label(P2, text="Elija el hotel que va a administrar:")
        hotel_label.grid(column=0, row=7, padx=1, pady=1)

        hotel_combobox = Combobox(P2, values=listaNombres, state="readonly")
        hotel_combobox.set("Hoteles")
        hotel_combobox.grid(column=1, row=7, padx=1, pady=1)
        
        endRegist = tk.Button(P2, text="Enviar")
        endRegist.place(relx=0.5, rely=0.3, anchor="n")
        endRegist.bind("<Button-1>", terminar)
        
        
    #Registro Empleado
    @classmethod
    def registroEmpleado(cls, root:Root):
        
        global nombre_entry
        global telefono_entry
        global username_entry
        global password_entry
        
        def compareName(event):
            rNom = False
            username = username_entry.get()  # Obtener el valor del Entry en tkinter
            for x in Base.getEmpleados():
                if x.getUsername() == username:
                    print("\nEste nombre ya está en uso. Intente de nuevo\n")
                    rNom = True
                    break
            if rNom == False:
                cont_button.destroy()
                nombre_entry["state"] = "disable"
                password_entry["state"] = "disable"
                username_entry["state"] = "disable"
                telefono_entry["state"] = "disable"
                cls.continueRegistroEmpleado(P2, root)
        
        root.title("SignUp")
        
        menuBar = Menu(root)
        root.config(menu=menuBar)
        archivo = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Archivo", menu=archivo)
        archivo.add_command(label="Salir", command=root.salir)
        
        signLabel = tk.Label(root, text="Registrarse", font=("arial", 30))
        signLabel.pack(side="top", padx=10, pady=10,)
        
        P1 = tk.Frame(root, bg="red")
        P1.pack(side="top", fill="both", expand=True)
        
        P2 = tk.Frame(P1, bg="blue", pady=10)
        P2.place(relx=0.5 ,relheight=1, anchor="n")
        nombre_label = tk.Label(P2, text="Ingrese su nombre completo:")
        nombre_label.grid(row=0, column=0, padx=1, pady=1)
        nombre_entry = tk.Entry(P2)
        nombre_entry.grid(row=0, column=1, padx=1, pady=1)
        
        telefono_label = tk.Label(P2, text="Ingrese su número de teléfono:")
        telefono_label.grid(row=1, column=0, padx=1, pady=1)
        telefono_entry = tk.Entry(P2)
        telefono_entry.grid(row=1, column=1, padx=1, pady=1)
        
        username_label = tk.Label(P2, text="Ingrese un nombre de usuario:")
        username_label.grid(row=2, column=0, padx=1, pady=1)
        username_entry = tk.Entry(P2)
        username_entry.grid(row=2, column=1, padx=1, pady=1)
        
        password_label = tk.Label(P2, text="Ingrese una contraseña:")
        password_label.grid(row=3, column=0, padx=1, pady=1)
        password_entry = tk.Entry(P2, show="*")  # Use show="*" to hide the password
        password_entry.grid(row=3, column=1, padx=1, pady=1)
        
        cont_button = tk.Button(P2, text="Continuar")
        cont_button.place(rely=0.2, relx=0.5, anchor="c")
        cont_button.bind("<Button-1>", compareName)
        
    
    @classmethod
    def continueRegistroEmpleado(cls, P2, root):
        def terminar(event):
            hotel = None
            selectedHotel = hotel_combobox.get()
            for x in hoteles:
                if x.getNombre() == selectedHotel:
                    hotel = x
            empleado = Empleado(nombre_entry.get(), telefono_entry.get(), username_entry.get(), password_entry.get(), CuentaBancaria(saldo_entry.get(), banco_entry.get()), hotel)
            Base.addEmpleados(empleado)
            
            if (is_bono_var):
                empleado.ofrecerBono()
            cls.intro(empleado)
            
            root.cleanRoot()
            Usmenu.menu(root, empleado)

        
        saldo_label = tk.Label(P2, text="Ingrese el saldo de su cuenta:")
        saldo_label.grid(column=0, row=4)

        saldo_entry = tk.Entry(P2)
        saldo_entry.grid(column=1, row=4)

        banco_label = tk.Label(P2, text="Ingrese el banco al que pertenece:")
        banco_label.grid(column=0, row=5)

        banco_entry = tk.Entry(P2)
        banco_entry.grid(column=1, row=5)
        
        listaNombres = []
        hoteles = Base.getHoteles()
        for x in hoteles:
            if x.getNombre() not in listaNombres:
                listaNombres.append(x.getNombre())
        
        hotel_label = tk.Label(P2, text="Elija el hotel en el que va a trabajar:")
        hotel_label.grid(column=0, row=6, padx=1, pady=1)

        hotel_combobox = Combobox(P2, values=listaNombres, state="readonly")
        hotel_combobox.set("Hoteles")
        hotel_combobox.grid(column=1, row=6, padx=1, pady=1)
        
        is_bono_label = tk.Label(P2, text="¿Quiere que se le envíe publicidad?")
        is_bono_label.grid(column=0, row=7, padx=1, pady=1)

        is_bono_var = tk.BooleanVar()
        cajon = tk.LabelFrame(P2)
        is_bono_radiobutton1 = tk.Radiobutton(cajon, text="Sí", variable=is_bono_var, value=True)
        is_bono_radiobutton2 = tk.Radiobutton(cajon, text="No", variable=is_bono_var, value=False)
        cajon.grid(column=1, row=7, padx=1, pady=1)
        is_bono_radiobutton1.pack(side="left")
        is_bono_radiobutton2.pack(side="right")
        
        endRegist = tk.Button(P2, text="Enviar")
        endRegist.place(relx=0.5, rely=0.5, anchor="n")
        endRegist.bind("<Button-1>", terminar)