from tkinter import *

class Start(Frame):
    def __init__(self, master, close_file,gtcredits):
        super(Start, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.close_file = close_file
        self.gtcredits = gtcredits

    def create_widgets(self):
        back = PhotoImage(file="Images-Blackjack/creditscreen.png")
        w = Label(self, image=back)
        w.photo = back
        w.grid(row=0, column=0, rowspan=16, columnspan=16)
        Label(self, text="Welcome to Blackjack!", fg="green",bg = "light goldenrod",font=31).grid(row=0, column=8, sticky=N)
        Button(self, text="Begin!", bg="green", font = 24,command=self.startgame).grid(row=3, column=8, sticky=N)
        Button(self,text = "Credits",bg = "green",font = 20,command= self.credits).grid(row =4, column =8,sticky = N)
    def startgame(self):
        self.close_file()
    def credits(self):
        self.gtcredits()