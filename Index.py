import tkinter
from tkinter import *
from Download import *


#crating a window with tkinter
root = Tk()
root.geometry('1024x600')
root.title("Deezloader")
root.config(bg='#ffffff')
root.iconbitmap('icon.ico')
photo = PhotoImage(file="icon2.png")
canvas = Canvas(root, width = 1024, height = 600, bg='#fff', bd=0, highlightthickness=0)
canvas.pack()
canvas.create_rectangle(0,0,512,600, fill="#ff0e7d", outline="#ff0e7d")
canvas.create_image(100,150, image=photo, anchor=NW)

#crating text input with tkinter

lab = Label(root, text="PLAY LIST YT:", font=("Helvetica", 20), bg='#ffffff')
lab.place(x=612, y=100)
Url = Entry(root, width=23, bg='#eee', fg='#000000', font=('Arial', 20), border=0, )

Url.place(x=612, y=150)

#crating boton with tkinter
def Download():
    Descargar(Url.get())

#rgb(236,236,236) in hex is #ececec
#crating boton with tkinter
Btn = Button(root, text="Download", width=10, height=1, bg='#eee', fg='#000', font=('Arial', 15), command=Download, bd=0)
Btn.place(x=712, y=350)



root.resizable(width=False, height=False)
root.mainloop()