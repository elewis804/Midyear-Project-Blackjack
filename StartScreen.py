from tkinter import *

class Start(Frame):
    def __init__(self, master, close_file):
        super(Start, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.close_file = close_file

    def create_widgets(self):
        back = PhotoImage(file="Images-Blackjack/creditscreen.png")
        w = Label(self, image=back)
        w.photo = back
        w.grid(row=0, column=0, rowspan=16, columnspan=16)
        Label(self, text="Welcome to Blackjack!", fg="green",bg = "light goldenrod",font=31).grid(row=0, column=8, sticky=N)
        Button(self, text="Begin!", bg="green", font = 24,command=self.startgame).grid(row=3, column=8, sticky=N)
    def startgame(self):
        self.close_file()
