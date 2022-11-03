# se importa la libreria tkinter con todas sus funciones 
from tkinter import *
from turtle import width
# ------------------
# Ventana principal 

ventana_principal=Tk()

# se ejecura el metodo mainloop() de la clase TK y queda a la espera de lo que el usuario haga cada accion del usuario de le conose como un evento.el metodo main loop es un bocle infinito

# titulo
ventana_principal.title("Sistemas uis")
#tamaño
ventana_principal.geometry("800x500")
# minimisar
ventana_principal.resizable(0,0)
# color
ventana_principal.config(bg="red")

frame_blanco = Frame(ventana_principal)
frame_blanco.config(bg="white",width=150,height=500)
frame_blanco.place(x=267,y=0)

frame_blanco2=Frame(ventana_principal)
frame_blanco2.place(x=0,y=150)
frame_blanco2.config(bg="white",width=800,height=150)

frame_azul=Frame(ventana_principal)
frame_azul.place(x=304,y=0)
frame_azul.config(bg="blue",width=75,height=500)

frame_azul2=Frame(ventana_principal)
frame_azul2.place(x=0,y=190)
frame_azul2.config(bg="blue",width=800,height=75)








ventana_principal.mainloop()