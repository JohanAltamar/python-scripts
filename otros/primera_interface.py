from tkinter import *

raiz = Tk() #Creacion de ventana
raiz.title("Calculadora") #Titulo
raiz.resizable(0,0) #Habilitar el cambio de tamaño (ancho, alto)
#para cambio de icono, utilizar conversor a .ico
#raiz.iconbitmap("nombre.ico")
raiz.geometry("650x350")#Ajsutar tamaño de ventana (ancho, alto)
raiz.config(bg = "blue")

raiz.mainloop() #Siempre al final
