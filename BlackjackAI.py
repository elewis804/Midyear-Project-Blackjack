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


    def begin(self):
        if self.rounds > 1:
            if self.turn == 1:
                self.switch["text"] = None
        if self.turn == 1:
            self.rounds += 1
            for x in self.player1.hand:
                self.player1.hand.remove(x)
            for x in self.player2.hand:
                self.player2.hand.remove(x)
            self.player1.score = 0
            self.player2.score = 0
        if self.rounds > 1:
            self.display_current.destroy()
        if self.turn == 1:
            self.player1.getRandomCard()
            self.player1.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand) - 1].image)
            self.player1.p_hand[len(self.player1.p_hand) - 1] = Label(self, image=card1)
            self.player1.p_hand[len(self.player1.p_hand) - 1].photo = card1
            self.player1.p_hand[len(self.player1.p_hand) - 1].grid(row=self.row, column=self.column)
            self.column += 1
            self.player1.getRandomCard()
            self.player1.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand) - 1].image)
            self.player1.p_hand[len(self.player1.p_hand) - 1] = Label(self, image=card1)
            self.player1.p_hand[len(self.player1.p_hand) - 1].photo = card1
            self.player1.p_hand[len(self.player1.p_hand) - 1].grid(row=self.row, column=self.column)
            self.column += 1
            if self.player1.score == 21:
                self.x = True
                self.blackjack = Button(self,text="Player 1 Blackjack",bg="indian red",command=self.stay,font=("Arial",16,"bold"))
                self.blackjack.grid(row=2,column=4,rowspan=2,columnspan=6)
        elif self.turn == 2:
            if not self.cleared:
                self.clear_board()
            else:
                self.cleared = False
            self.player2.getRandomCard()
            self.player2.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player2.hand[len(self.player2.hand) - 1].image)
            self.player2.p_hand[len(self.player2.p_hand) - 1] = Label(self, image=card1)
            self.player2.p_hand[len(self.player2.p_hand) - 1].photo = card1
            self.player2.p_hand[len(self.player2.p_hand) - 1].grid(row=self.row, column=self.column)
            self.column += 1
            self.player2.getRandomCard()
            self.player2.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player2.hand[len(self.player2.hand) - 1].image)
            self.player2.p_hand[len(self.player2.p_hand) - 1] = Label(self, image=card1)
            self.player2.p_hand[len(self.player2.p_hand) - 1].photo = card1
            self.player2.p_hand[len(self.player2.p_hand) - 1].grid(row=self.row, column=self.column)
            self.column += 1
            if self.player2.score == 21:
                self.x = True
                self.blackjack = Button(self,text="Player 2 Blackjack",bg="sky blue",command=self.stay,font=("Arial",16,"bold"))
                self.blackjack.grid(row=2,column=4,rowspan=2,columnspan=6)
        self.start.destroy()
        if not self.x:
            self.h = Button(self,text="Hit",command=self.Hit)
            self.h.grid(row=2,column=14,sticky=E)
            self.s = Button(self,text="Stay",command=self.stay)
            self.s.grid(row=2,column=0,sticky=W)
    
    def turn_switch(self,to):
        '''This method will display a constant label showing whose turn it is'''
        if self.turn < 3:
            self.switch = Label(self,text=("Turn: Player " + str(to)),font=("Times",16,"bold"))
            self.switch.grid(row=11,column=7,sticky=N)
        else:
            self.switch.destroy()
            self.switch = Label(self,text=("Round Over"),font=("Times",16,"bold"))
            self.switch.grid(row=11,column=7,sticky=N)
            self.round_end()
    
    def Hit(self):
        if self.turn == 1:
            self.player1.getRandomCard()
            if self.player1.score <= 20:
                self.player1.p_hand.append(0)
                if self.column < 4:
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand) - 1].image)
                    self.player1.p_hand[len(self.player1.p_hand) - 1] = Label(self, image=card1)
                    self.player1.p_hand[len(self.player1.p_hand) - 1].photo = card1
                    self.player1.p_hand[len(self.player1.p_hand) - 1].grid(row=self.row, column=self.column)
                    self.column += 1
                else:
                    self.row += 2
                    self.column = 1
                    self.player1.p_hand.append(0)
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand) - 1].image)
                    self.player1.p_hand[len(self.player1.p_hand) - 1] = Label(self, image=card1)
                    self.player1.p_hand[len(self.player1.p_hand) - 1].photo = card1
                    self.player1.p_hand[len(self.player1.p_hand) - 1].grid(row=self.row, column=self.column)
            else:
                self.turn = 2
                self.player1.bust = True
                self.clear_board()
                self.cleared = True
                self.turn_switch(self.turn)
                self.start = Button(self, text="Player " + str(self.turn) + " start turn", bg ="sky blue",command=self.begin,
                                    font=("Arial", 30, "bold"))
                self.start.grid(row=5, column=6)
                self.h.destroy()
                self.s.destroy()
        elif self.turn == 2:
            self.player2.getRandomCard()
            if self.player2.score <= 20:
                self.player2.p_hand.append(0)
                if self.column < 4:
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player2.hand[len(self.player2.hand) - 1].image)
                    self.player2.p_hand[len(self.player2.p_hand) - 1] = Label(self, image=card1)
                    self.player2.p_hand[len(self.player2.p_hand) - 1].photo = card1
                    self.player2.p_hand[len(self.player2.p_hand) - 1].grid(row=self.row, column=self.column)
                    self.column += 1
                else:
                    self.row += 2
                    self.column = 1
                    self.player1.p_hand.append(0)
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand) - 1].image)
                    self.player1.p_hand[len(self.player1.p_hand) - 1] = Label(self, image=card1)
                    self.player1.p_hand[len(self.player1.p_hand) - 1].photo = card1
                    self.player1.p_hand[len(self.player1.p_hand) - 1].grid(row=self.row, column=self.column)
            else:
                self.turn = 3
                self.player2.bust = True
                self.clear_board()
                self.cleared = True
                self.turn_switch(self.turn)
                self.h.destroy()
                self.s.destroy()
                for x in range(len(self.player2.p_hand)):
                    self.player2.p_hand[x].destroy()
                for x in self.player2.p_hand:
                    self.player2.p_hand.remove(x)
    