from tkinter import *

window = Tk("My First Program")
label = Label(window,text = "Welcome to Python GUI ... ")
button = Button(window,text = "OK")
label.pack()
button.pack()
window.mainloop()
