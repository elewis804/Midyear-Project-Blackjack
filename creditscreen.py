from tkinter import *

class Credit(Frame):
    def __init__(self, master):
        super(Credit, self).__init__(master)
        self.grid()
        self.create_widgets()
        quill = PhotoImage(file="Images-Blackjack/creditscreen.png")
        q = Label(self, image=quill)
        q.photo = quill
        q.grid(row=0, column=0, rowspan=15, columnspan=15)


    def create_widgets(self):
        Label(text = "Made by Benen Sullivan, Lukas Tegge, Hayun Jung, and Eric Lewis  ", bg = 'gold', font = ("Arial",19, "bold")).grid(row = 1, column = 0, sticky = W )
