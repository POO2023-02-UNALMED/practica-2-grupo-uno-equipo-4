import sys
from tkinter import Menu, messagebox
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
from errores.ErrorEmpty import ErrorEmpty

#@autor: David Restrepo

class Login():
    @classmethod
    def login(cls, root:Root):
        
        
        def continuar(event):
            correct = True
            if (usType.get() == "Tipo"):
                er = ErrorEmpty(usType.get())
                text = er.mostrarMensaje()
                messagebox.showerror("Error", text)
                correct = False
            for i in entries:
                val = i.get()
                if val == "":
                    er = ErrorEmpty(i.widget_name)
                    text = er.mostrarMensaje()
                    messagebox.showerror("Error", text)
                    correct = False
            
            if correct:
                if (usType.get() == "Huesped"):
                    correctRegist = False
                    username = username_entry.get()
                    password = password_entry.get()
                    for x in Base.getHuespedes():
                        if x.getUsername() == username and x.getPassword() == password:
                            cls.avisoEntrada(x)
                            correctRegist = True
                            root.cleanRoot()
                            Usmenu.menu(root, x)
                            break
                    if correctRegist == False:
                        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")
                        print("Nombre de usuario o contraseña incorrectos")
                        
                
                elif usType.get() == "Administrador":
                    correctRegist = False
                    username = username_entry.get()
                    password = password_entry.get()
                    for x in Base.getAdministradores():
                        if x.getUsername() == username and x.getPassword() == password:
                            cls.avisoEntrada(x)
                            correctRegist = True
                            root.cleanRoot()
                            Usmenu.menu(root, x)
                            break
                    if correctRegist == False:
                        print("Nombre de usuario o contraseña incorrectos")
                        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")
                
                else:
                    correctRegist = False
                    username = username_entry.get()
                    password = password_entry.get()
                    for x in Base.getEmpleados():
                        if x.getUsername() == username and x.getPassword() == password:
                            cls.avisoEntrada(x)
                            correctRegist = True
                            root.cleanRoot()
                            Usmenu.menu(root, x)
                            break
                    if correctRegist == False:
                        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")
                        print("Nombre de usuario o contraseña incorrectos")
        
        
        entries = []
        root.title("LogIn")
        
        menuBar = Menu(root)
        root.config(menu=menuBar)
        archivo = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Archivo", menu=archivo)
        archivo.add_command(label="Salir", command=root.salir)
        
        signLabel = tk.Label(root, text="Iniciar sesión", font=("arial", 25))
        signLabel.pack(side="top", padx=10, pady=10,)
        
        #Seleccionar que tipo de usuario es
        P1 = tk.Frame(root, bg="red")
        P1.pack(side="top", fill="both", expand=True)
        P2 = tk.Frame(P1, bg="yellow")
        P2.place(relx=0.5, rely=0.14, relheight=0.25, anchor="c")
        # P2.pack(anchor="c", pady=10, fill="y")
        typesLabel = tk.Label(P2, text="Tipo de usuario:")
        typesLabel.grid(row=0, column=0, padx=1, pady=1)
        types = ["Huesped", "Administrador", "Empleado"]
        usType = Combobox(P2, values=types, state="readonly",font=("arial", 10))
        usType.set("Tipo")
        usType.grid(row=0, column=1, padx=1, pady=1)
                
        username_label = tk.Label(P2, text="Ingrese su nombre de usuario:")
        username_label.grid(row=1, column=0, padx=1, pady=1)
        username_entry = tk.Entry(P2)
        username_entry.grid(row=1, column=1, padx=1, pady=1)
        username_entry.widget_name = "username"
        entries.append(username_entry)
        
        password_label = tk.Label(P2, text="Ingrese su contraseña:")
        password_label.grid(row=2, column=0, padx=1, pady=1)
        password_entry = tk.Entry(P2, show="*")  # Use show="*" to hide the password
        password_entry.grid(row=2, column=1, padx=1, pady=1)
        password_entry.widget_name = "password"
        entries.append(password_entry)
        
        cont = tk.Button(P2, text="Continuar")
        cont.place(y=100, relx=0.5, anchor="c")
        cont.bind("<Button-1>", continuar)
        
    @classmethod
    def avisoEntrada(cls, usuario):
        print(usuario.entrando())