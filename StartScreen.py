from tkinter import *

class Start(Frame):
<<<<<<< HEAD
    def __init__(self, master, close_file1, close_file2):
        super(Start, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.close_file1 = close_file1
        self.close_file2 = close_file2
=======
    def __init__(self, master, close_file,gtcredits):
        super(Start, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.close_file = close_file
        self.gtcredits = gtcredits
>>>>>>> ad22e4a39f39e670871f82214952b75c4416d3ed

    def create_widgets(self):
        back = PhotoImage(file="Images-Blackjack/creditscreen.png")
        w = Label(self, image=back)
        w.photo = back
        w.grid(row=0, column=0, rowspan=16, columnspan=16)
        Label(self, text="Welcome to Blackjack!", fg="green",bg = "light goldenrod",font=31).grid(row=0, column=8, sticky=N)
<<<<<<< HEAD
        self.tpButton = Button(self, text="2 Player", bg="green", font = 24,command=self.startgame2P)
        self.tpButton.grid(row=3, column=8, sticky=N)
        self.AIButton = Button(self, text="1 Player", bg="green", font=24, command=self.startgame1P)
        self.AIButton.grid(row=4, column=8, sticky=N)
    def startgame2P(self):
        self.close_file1()
    
    def startgame1P(self):
        self.close_file2()
=======
        Button(self, text="Begin!", bg="green", font = 24,command=self.startgame).grid(row=3, column=8, sticky=N)
        Button(self,text = "Credits",bg = "green",font = 20,command= self.credits).grid(row =4, column =8,sticky = N)
    def startgame(self):
        self.close_file()
    def credits(self):
        self.gtcredits()
>>>>>>> ad22e4a39f39e670871f82214952b75c4416d3ed
