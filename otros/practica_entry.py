#https://www.youtube.com/watch?v=nZF9SwhmPRo
from tkinter import *
root = Tk()
myFrame = Frame(root, width=1200, height=600)
myFrame.pack()

minombre=StringVar()

EditNombre=Entry(myFrame, textvariable = minombre)
#EditText.place(x=100, y=100)
EditNombre.grid(row=0, column=1, padx=10, pady=10)

EditApellido=Entry(myFrame)
EditApellido.grid(row=1, column=1, padx=10, pady=10)

EditPass=Entry(myFrame)
EditPass.grid(row=2, column=1, padx=10, pady=10)
EditPass.config(show="*")

EditDireccion=Entry(myFrame)
EditDireccion.grid(row=3, column=1, padx=10, pady=10)

EditComentarios=Text(myFrame, width=16, height=5)
EditComentarios.grid(row=4, column=1, padx=10, pady=10)
ScrollVert = Scrollbar(myFrame, command=EditComentarios.yview)
ScrollVert.grid(row=4, column=2, sticky="nsew")
EditComentarios.config(yscrollcommand=ScrollVert.set)

NameLabel = Label(myFrame, text="Nombre: ")
NameLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

ApellidoLabel = Label(myFrame, text="Apellido: ")
ApellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

PassLabel = Label(myFrame, text="Password: ")
PassLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

DireccionLabel = Label(myFrame, text="Direccion: ")
DireccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

CommentariosLabel = Label(myFrame, text="Comentarios: ")
CommentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

def codigoBoton():
	minombre.set("Johan")

boton=Button(root,text="Enviar", command=codigoBoton)
boton.pack()

root.mainloop()