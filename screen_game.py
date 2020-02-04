from tkinter import *
import time
from Blackjackinteractions import Player

'''
TO DO:
FIX THE IMAGES SO THEY ARE ALL SAME SIZES'''

class ScreenGame(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.row = 5
        self.column = 5
        self.rounds = 0
        self.player1 = Player()
        self.player2 = Player()
        self.turn = 1
        self.grid()
        back = PhotoImage(file="Images-Blackjack/dealertable.png")
        w = Label(self, image=back)
        w.photo = back
        w.grid(row=0, column=0, rowspan=15,columnspan=15)
        self.start = Button(self,text="Player " + str(self.turn) + "Start turn",command=self.begin,font=("Arial",30,"bold"))
        self.start.grid(row=5,column=6)


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
                self.h.destroy()
                self.s.destroy()
                self.player1.bust = True
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
                self.turn_switch(self.turn)
                self.h.destroy()
                self.s.destroy()
                self.player2.bust = True

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
            self.start.grid(row=5, column=6)
            self.h.destroy()
            self.s.destroy()
        else:
            self.round_end()
            self.turn_switch(self.turn)
            self.h.destroy()
            self.s.destroy()

    def update_score(self,wins):
        if self.rounds > (self.player1.win + self.player2.win):
            wins += 1


    def round_end(self):
        if self.player1.bust:
            if self.player2.bust:
                self.display_current = Label(self,text="Tie Round")
                self.display_current.grid(row=13,column=7,sticky=S)
            else:
                self.display_current = Label(self,text="Player 2 Wins Round")
                self.display_current.grid(row=13,column=7,sticky=S)
                self.update_score(self.player2.win)
        elif self.player2.bust:
            self.display_current = Label(self,text="PLayer 1 Wins Round")
            self.display_current.grid(row=13,column=7,sticky=S)
            self.update_score(self.player2.win)
        else:
            if self.player1.score > self.player2.score:
                self.display_current = Label(self,text="Player 1 Wins Round")
                self.display_current.grid(row=13,column=7,sticky=S)
                self.update_score(self.player1.win)
            elif self.player2.score > self.player1.score:
                self.display_current = Label(self,text="Player 2 Wins Round")
                self.display_current.grid(row=13,column=7,sticky=S)
                self.update_score(self.player2.win)
            else:
                self.display_current = Label(self,text="Tie Round")
                self.display_current.grid(row=13,column=7,sticky=S)

    def turn_switch(self,to):
        '''This method will display a constant label showing whose turn it is'''
        if self.turn < 3:
            self.switch = Label(self,text=("Turn: Player" + str(to)),font=("Times",16,"bold"))
            self.switch.grid(row=11,column=7,sticky=S)
        else:
            self.switch.destroy()
            self.switch = Label(self,text=("Turn Over"),font=("Times",16,"bold"))
            self.switch.grid(row=11,column=7,sticky=S)
            self.round_end()
            self.score_display()



    def begin(self):
        self.rounds += 1
        if self.turn == 1:
            self.player1.getRandomCard()
            self.player1.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand) - 1].image)
            self.player1.p_hand[len(self.player1.p_hand) - 1] = Label(self, image=card1)
            self.player1.p_hand[len(self.player1.p_hand) - 1].photo = card1
            self.player1.p_hand[len(self.player1.p_hand) - 1].grid(row=self.row, column=self.column)
            self.player1.getRandomCard()
            self.player1.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand) - 1].image)
            self.player1.p_hand[len(self.player1.p_hand) - 1] = Label(self, image=card1)
            self.player1.p_hand[len(self.player1.p_hand) - 1].photo = card1
            self.player1.p_hand[len(self.player1.p_hand) - 1].grid(row=self.row, column=self.column+1)
        elif self.turn == 2:
            self.player2.getRandomCard()
            self.player2.getRandomCard()
        self.start.destroy()
        self.h = Button(self,text="Hit",command=self.Hit)
        self.h.grid(row=2,column=14,sticky=E)
        self.s = Button(self,text="Stay",command=self.stay)
        self.s.grid(row=2,column=0,sticky=W)
        self.player1.getRandomCard()
        self.player1.p_hand.append(0)
        card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand)-1].image)
        self.player1.p_hand[len(self.player1.p_hand)-1] = Label(self, image=card1)
        self.player1.p_hand[len(self.player1.p_hand)-1].photo = card1
        self.player1.p_hand[len(self.player1.p_hand)-1].grid(row=5,column=5)

    def score_display(self):
        self.p1_wins = Label(self,text=self.player1.win,font=("Times",12))
        self.p1_wins.grid(row=0,column=5,sticky=N)
        self.p2_wins = Label(self,text=self.player2.win,font=("Times",12))
        self.p2_wins.grid(row=0,column=8,sticky=N)