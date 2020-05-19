from tkinter import *

root=Tk()
miFrame = Frame(root, width="500", height="400")
miFrame.pack()

Titulo = Label(miFrame, text="Software de Control de Ventas", fg="red", font=("Comic Sans MS",18))
Titulo.place(x="100",y="5")
#miImagen=PhotoImage(file="mouse.gif")
#Label(miFrame, image=miImagen).place(x="100",y="200")

root.mainloop()