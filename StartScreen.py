from tkinter import *

class Start(Frame):
    def __init__(self, master, close_file1, close_file2, close_file3, gtcredits):
        super(Start, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.close_file1 = close_file1
        self.close_file2 = close_file2
        self.close_file3 = close_file3
        self.gtcredits = gtcredits

    def create_widgets(self):
        back = PhotoImage(file="Images-Blackjack/creditscreen.png")
        w = Label(self, image=back)
        w.photo = back
        w.grid(row=0, column=0, rowspan=16, columnspan=16)
        Label(self, text="Welcome to Blackjack!", fg="green",bg = "light goldenrod",font=31).grid(row=0, column=8, sticky=N)
        self.tpButton = Button(self, text="2 Player", bg="green", font = 24,command=self.startgame2P)
        self.tpButton.grid(row=3, column=8, sticky=N)
        self.AIButton = Button(self, text="1 Player", bg="green", font=24, command=self.startgame1P)
        self.AIButton.grid(row=4, column=8, sticky=N)
        self.multi = Button(self,text="4 PLayer",bg="green",font=24,command=self.startgame4p)
        self.multi.grid(row=4,column=8,sticky=N)
        self.creditButton = Button(self, text="Credits", bg="red", font=24, command=self.credits)
        self.creditButton.grid(row=5, column=8, sticky=N)
    
    def startgame2P(self):
        self.close_file1()
    
    def startgame1P(self):
        self.close_file2()

    def startgame4p(self):
        self.close_file3()

    def credits(self):
        self.gtcredits()
