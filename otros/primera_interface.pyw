from tkinter import *

raiz = Tk() #Creacion de ventana
raiz.title("Calculadora") #Titulo
#raiz.resizable(0,0) #Habilitar el cambio de tamaño (ancho, alto)
#para cambio de icono, utilizar conversor a .ico
#raiz.iconbitmap("nombre.ico")
#LA VENTANA Tk SE AJUSTA AL TAMAÑO DE SU CONTENERDOR INTERNO
#raiz.geometry("650x350")#Ajsutar tamaño de ventana (ancho, alto)
raiz.config(bg = "gray")#Cambiar parametros

miFrame = Frame() #Crear Frame
miFrame.pack(fill="both", expand=1) #Empaquetar frame con ventana Tk
miFrame.config(width="650",height="320", bg = "red")


raiz.mainloop() #Siempre al final
