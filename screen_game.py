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
        self.player1.getRandomCard()
        self.player1.getRandomCard()
        self.player2.getRandomCard()
        self.player2.getRandomCard()
        self.turn = 1
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        back = PhotoImage(file="Images-Blackjack/dealertable.png")
        w = Label(self, image=back)
        w.photo = back
        w.grid(row=0, column=0, rowspan=15,columnspan=15)

        self.start = Button(self,text="Player " + str(self.turn) + "Start turn",command=self.begin,font=("Arial",30,"bold"))
        self.start.grid(row=3,column=6)


    def Hit(self):
        if self.turn == 1:
            if self.player1.score <= 20:
                self.player1.getRandomCard()
                self.player1.p_hand.append(0)
                card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand)-1].image)
                self.player1.p_hand[len(self.player1.p_hand)-1] = Label(self, image=card1)
                self.player1.p_hand[len(self.player1.p_hand)-1].photo = card1
                self.player1.p_hand[len(self.player1.p_hand)-1].grid(row=5,column=5)
            else:
                self.turn = 2
                self.turn_switch(self.turn)
        elif self.turn == 2:
            if self.player2.score <= 20:
                self.player2.getRandomCard()
                self.player2.p_hand.append(0)
                card1 = PhotoImage(file="Images-Blackjack/" + self.player2.hand[len(self.player2.hand)-1].image)
                self.player2.p_hand[len(self.player2.p_hand)-1] = Label(self, image=card1)
                self.player2.p_hand[len(self.player2.p_hand)-1].photo = card1
                self.player2.p_hand[len(self.player2.p_hand)-1].grid(row=5,column=5)
            else:
                self.turn = 3

    def stay(self):
        if self.turn == 1:
            for x in range(len(self.player1.p_hand)):
                self.player1.p_hand[x].destroy()
            for x in self.player1.p_hand:
                self.player1.p_hand.remove(x)
        elif self.turn == 2:
            for x in range(len(self.player2.p_hand)):
                self.player2.p_hand[x].destroy()
            for x in self.player2.p_hand:
                self.player2.p_hand.remove(x)
        self.turn += 1
        if self.turn < 3:
            self.turn_switch(self.turn)
            self.start = Button(self, text="Player " + str(self.turn) + "Start turn", command=self.begin,
                                font=("Arial", 30, "bold"))
            self.start.grid(row=3, column=6)
            self.h.destroy()
            self.s.destroy()
        else:
            self.turn_switch(self.turn)
            self.h.destroy()
            self.s.destroy()



    def turn_switch(self,to):
        '''This method will display a constant label showing whose turn it is'''
        if self.turn < 3:
            self.switch = Label(self,text=("Turn: Player" + str(to)),font=("Times",16,"bold"))
            self.switch.grid(row=11,column=7,sticky=S)
        else:
            self.switch.destroy()
            self.switch = Label(self,text=("Turn Over"),font=("Times",16,"bold"))
            self.switch.grid(row=11,column=7,sticky=S)

    def begin(self):
        self.start.destroy()
        self.h = Button(self,text="Hit",command=self.Hit)
        self.h.grid(row=2,column=14,sticky=E)
        self.s = Button(self,text="Stay",command=self.stay)
        self.s.grid(row=2,column=0,sticky=W)