# !/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from googletrans import Translator

class Traductor:
    def __init__(self):
        
        self.ventana1=tk.Tk()
        self.ventana1.geometry("900x600")
        self.ventana1.columnconfigure(0, weight=1)
        self.ventana1.rowconfigure(0, weight=1)
        self.ventana1.rowconfigure(10, weight=1)
        self.ventana1.title("Traductor Multiple.")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        #Paginas del notebook
        self.menu()
        self.traducir1()
        self.cuaderno1.grid(column=0, row=0, sticky="nsew")
        self.ventana1.mainloop()    

    def menu(self):
        self.menu=Menu(self.ventana1)
        self.ventana1.config(menu=self.menu)
        self.archivo = Menu(self.menu, tearoff=1)
        self.archivo.add_command(label="Parto Normal",command=lambda: self.seleccion(1))
        self.archivo.add_command(label="Cesarea",command=lambda: self.seleccion(2))
        self.archivo.add_separator()
        self.archivo.add_command(label="Salir", command=lambda: self.salir())
        self.Acerca_De = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=self.archivo)
        self.Acerca_De.add_command(label="Autor", command=lambda: self.mensajes(1))
        self.Acerca_De.add_command(label="Frase", command=lambda: self.mensajes(2))
        self.Acerca_De.add_command(label="Desarrollador",command=lambda: self.mensajes(3))
        self.menu.add_cascade(label="Acerca de",menu=self.Acerca_De)
   


    def seleccion(self,opc):
        if opc == 1:
                mb.showinfo("Alerta","Usted ya esta en el formulario de parto normal")
        elif opc == 2:
            print("hola")
        else:
            print("asd")


    def salir(self):
        
        accion = mb.askyesno("Advertencia",
                                   "¿Seguro que desea cerrar el programa?\n Todos los cambios no guardados se perderan")
        if accion == True:
            self.ventana1.destroy()

    def mensajes(self,opc):
        if opc==1:
            mb.showinfo("", "")
        if opc==2:
            mb.showinfo("Frase", "Todo hombre fuerte fue debil alguna vez, asi que la proxima vez que lo pienses no me subestimes"
                                       " que aun estoy en el juego")
        if opc==3:
            mb.showinfo("Desarrollador","Nombre: Jesus Delgado\n""21004289\n""Ing. En Sistemas\n")

    def traducir1(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="")
        self.cuaderno1.add(self.pagina1, text="Traductor")        
        self.labelframe1.grid(column=1, row=1,columnspan=7, sticky="nsew",padx=5, pady=5, ipadx=5, ipady=5)

        
#-----------DATOS DEL PACIENTE--------------------------------------------------

        self.label1=ttk.Label(self.labelframe1, text="Texto a Traducir:")
        self.label1.grid(column=0, row=0)
        self.textocarga=tk.StringVar()
        self.entrydtexto=ttk.Entry(self.labelframe1, textvariable=self.textocarga)
        self.entrydtexto.grid(column=1, row=0)
        
        self.label2=ttk.Label(self.labelframe1, text="Idioma:")        
        self.label2.grid(column=2, row=0, padx=4, pady=4)
        self.combo = ttk.Combobox(self.labelframe1,values=[u"Seleciona","Español",
        													 "Ingles", "Italiano"])
        self.combo.current(1) #set the selected item
        self.combo.grid(column=3, row=0)

        self.label3=ttk.Label(self.labelframe1, text="Idioma:")        
        self.label3.grid(column=4, row=0, padx=4, pady=4)
        self.combo2 = ttk.Combobox(self.labelframe1,values=[u"Seleciona","Español",
        													 "Ingles", "Italiano"])
        self.combo2.current(1) #set the selected item
        self.combo2.grid(column=5, row=0)
        
        """self.idiomacarga=tk.StringVar()
        self.entryidioma=ttk.Entry(self.labelframe1, textvariable=self.idiomacarga)
        self.entryidioma.grid(column=3, row=0, padx=4, pady=4)
		"""
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar",command=self.cambiar)
        self.boton1.grid(column=0, row=1, padx=4, pady=4, columnspan=1, sticky="we")


    def cambiar(self):
    	if self.combo.get() == u"Español":
    		self.idioma = "es"
    	elif self.combo.get() == "Ingles":
    		self.idioma = "en"
    	elif self.combo.get() == "Italiano":
    		self.idioma = "it"
    	if self.combo2.get() == u"Español":
    		self.idioma2 = "es"
    	elif self.combo2.get() == "Ingles":
    		self.idioma2 = "en"
    	elif self.combo2.get() == "Italiano":
    		self.idioma2 = "it"
    	self.traductor = Translator()
    	self.resultado = self.traductor.translate(self.textocarga.get(),src=self.idioma,dest=self.idioma2)
    	if self.idioma == "es" and self.idioma2 == "en":
    		self.resultado2 = str(self.resultado).strip(u'Translated(src= es,dest=en,text= ')
    	else:
    		self.resultado2 = str(self.resultado).strip(u'Translated(src=es, dest=it,text= ')
    	mb.showinfo("Traduccion", str(self.resultado2))


aplicacion1=Traductor()




