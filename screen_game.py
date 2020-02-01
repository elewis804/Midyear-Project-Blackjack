from tkinter import *
import time
from Blackjackinteractions import Player

'''
TO DO:
FIX THE IMAGES SO THEY ARE ALL SAME SIZES'''

class ScreenGame(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.player1 = Player()
        self.player2 = Player()
        self.turn = 1
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        back = PhotoImage(file="Images-Blackjack/dealertable.png")
        w = Label(self, image=back)
        w.photo = back
        w.grid(row=0, column=0, rowspan=15,columnspan=15)

        Button(self,text="Hit",command=self.Hit).grid(row=3,column=14,sticky=E)
        Button(self,text="Stay",command=self.stay).grid(row=3,column=0,sticky=W)


    def Hit(self):
        if self.turn == 1:
            if self.player1.score <= 20:
                self.player1.getRandomCard()
                card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand)-1].image)
                x = Label(self, image=card1)
                x.photo = card1
                x.grid(row=5,column=3,rowspan=2,columnspan=2)

            else:
                self.turn = 2
                self.turn_switch(self.turn)
        elif self.turn == 2:
            if self.player2.score <= 20:
                self.player2.getRandomCard()
            else:
                self.turn = 3

    def stay(self):
        self.turn += 1
        if self.turn < 3:
            self.turn_switch(self.turn)


    def turn_switch(self,to):
        '''This method will display a constant label showing whose turn it is'''
        self.switch = Label(self,text=("Turn: Player" + str(to)),font=24)
        self.switch.grid(row=14,column=7,sticky=S)

