from tkinter import *

class WidgetDemo():
    def __init__(self):
        window = Tk()
        window.title("Widgets Demo !")
        frame1 = Frame(window)
        frame1.pack()

        self.v1 = IntVar()
        cbtnBold = Checkbutton(frame1,text = "Bold", variable=self.v1, command = self.processCheckbutton)
        self.v2 = IntVar()
        rbtnBlue = Radiobutton(frame1, text = "Blue", variable=self.v2, value=1, command = self.processRadiobutton)
        rbtnRed = Radiobutton(frame1, text = "Red", variable=self.v2, value=2,command = self.processRadiobutton)

        cbtnBold.grid(row = 1, column = 1)
        rbtnBlue.grid(row = 1, column = 2)
        rbtnRed.grid(row = 1, column = 3)

        frame2 = Frame(window)
        frame2.pack()

        self.label = Label(frame2, text = "Enter your Name ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name)
        btnSubmitName = Button(frame2, text = "Submit Name", command = self.processNamebutton)
        message = Message(frame2, text = "THis is just a demo ")

        frame3 = Frame(window)
        frame3.pack()
        self.welcomeLabel = Label(frame3, text = "Welcome !")
        self.label.grid(row = 1, column=1)
        entryName.grid(row = 1, column = 2)
        btnSubmitName.grid(row = 1, column = 3)
        #message.grid(row = 2, column = 1)
        self.welcomeLabel.grid(row =1, column = 1)
        

        self.text = Text(window)
        self.text.pack()
        self.text.insert(END, "Thank you for using whatever !!")

        window.mainloop()

    def processCheckbutton(self):
        print("Check Button pressed ", self.v1.get())
    def processRadiobutton(self):
        if (self.v2.get() == 2):
            self.text["fg"] = "Red"
            self.text["bg"] = "#FFAABB"
        print("Radio Button Pressed ", self.v2.get())
    def processNamebutton(self):
        self.welcomeLabel["text"] = "Welcome " + self.name.get() + "!!!!"
        print("Name Button is pressed ", self.name.get())

WidgetDemo()
