from tkinter import *

class Start(Frame):
    def __init__(self, master, close_file):
        super(Start, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.close_file = close_file

    def create_widgets(self):
        Label(self, text="Welcome to Blackjack!", fg="green", font=31).grid(row=0, column=0, sticky=N)
        Label(self, text="Made by Erik Lewis, Benen Sullivan, Lukas Tegge, and Hayun Jung").grid(row=1, column=0, sticky=N)
        Button(self, text="Begin!", bg="green", command=self.startgame).grid(row=2, column=0, sticky=N)

    def startgame(self):
        self.close_file()

