from tkinter import *

def processEventOK():
    print("OK Pressed !!!")
def processEventCancel():
    print("Cancel Button Pressed !!!")
    
window = Tk()
label = Label(window,text="This is a processing Event and Functions Created")
btnOK = Button(window,text="OK", fg="blue", command = processEventOK)
btnCancel = Button(window, text="Cancel", fg="red", command = processEventCancel)
label.pack()
btnOK.pack()
btnCancel.pack()
window.mainloop()
