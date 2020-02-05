from tkinter import *

class Credit(Frame):
    def __init__(self, master):
        super(Credit, self).__init__(master)
        self.grid()
        self.create_widgets()
        back = PhotoImage(file="Images-Blackgack/creditscreen.png")
        w = Label(self, image=back)
        w.photo = back
        w.grid(row=0, column=0, rowspan=15, columnspan=15)


    def create_widgets(self):
        Label(text = "Made by Benen Sullivan, Lukas Tegge, Hayun Jung, and Eric Lewis", font = 31).grid(row = 1, columnn = 1, sticky = W )
