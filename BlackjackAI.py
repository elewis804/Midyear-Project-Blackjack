from tkinter import *
from Blackjackinteractions import Player

class AIGame(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.row = 5
        self.column = 1
        self.rounds = 0
        self.player1 = Player()
        self.player2 = Player()
        self.turn = 1
        self.ties = 0
        self.cleared = False
        self.x = False
        self.end = False
        self.grid()
        back = PhotoImage(file="Images-Blackjack/dealertable.png")
        w = Label(self, image=back)
        w.photo = back
        w.grid(row=0, column=0, rowspan=15,columnspan=15)
        self.start = Button(self,text="Player Start turn", bg = "indian red",font=("Arial",30,"bold"))
        self.start.grid(row=5,column=6)