from tkinter import *

#@autor: David Restrepo

class FieldFrame(Frame):        #FieldFrame
    
    def __init__ (self, tituloCriterios, criterios, tituloValores, valores = None, habilitado = None) :
        
        self.listaValores = []
        self.func = None
        
        def borrarText():
            for j in self.entries:
                j.delete(0, END)
                
        
        def comprobar():
            # incorrect = False
            # for k in self.entries:
            #     ind = self.entries.index(k)
            #     if valores != None:
            #         if valores[ind] == "int":
            #             try:
            #                 numero_entero = int(k.get())
            #             except ValueError:
            #                 incorrect = True
            #                 print(f"Debe ingresar un valor correcto en la casilla {criterios[ind]}")
            #         elif type(k.get()).__name__ != valores[ind]:
            #             print(f"Debe ingresar un valor correcto en la casilla {criterios[ind]}")
            #             incorrect = True
            # if incorrect == False:
            entriesValues = []
            for l in self.entries:
                entriesValues.append(l.get())
            self.listaValores = entriesValues
            if self.func != None:
                print(self.listaValores)
                self.func(self.listaValores)
        
        self.entries = []
        
        self.p1 = Frame()
        self.p1.pack(anchor="center", ipadx=10, ipady=10)
        
        titulo1 = Label(self.p1, text=tituloCriterios)
        titulo1.grid(row=0, column=0, padx=10, pady=10)
        
        titulo2 = Label(self.p1, text=tituloValores)
        titulo2.grid(row=0, column=1, padx=10, pady=10)
        
        
        for i in criterios:
            ind = criterios.index(i)
            
            label = Label(self.p1, text=i)
            label.grid(row=ind+1, column=0, padx=10, pady=10)
            
            entry = Entry(self.p1)
            entry.grid(row=ind+1, column=1, padx=10, pady=10)
            if valores != None:
                entry.insert(0, valores[ind])
            self.entries.append(entry)
                
            if habilitado != None:
                if i in habilitado:
                    entry.config(state="disabled")
            
            if i == "Codigo" or i == "codigo":
                entry.config(state="disabled")
                    
        aceptar = Button(self.p1, text="Aceptar", command=comprobar)
        aceptar.grid(row=len(criterios)+1, column=0, padx=10, pady=10)
        borrar = Button(self.p1, text="Borrar", command=borrarText)
        borrar.grid(row=len(criterios)+1, column=1, padx=10, pady=10)
                
                
    def setRoot(self, root):
        self.p1.pack(in_=root)
        
    def setFunc(self, func):
        self.func = func
            
    def getFrame(self):
        return self.p1
            
    def getValores(self):
        if self.listaValores != []:
            return self.listValores
        else:
            print("No hay valores disponibles")
            return None
    
    