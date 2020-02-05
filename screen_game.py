from tkinter import *
import time
from Blackjackinteractions import Player

'''TO DO:
Fix Round over not disappearing'''
class ScreenGame(Frame):
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
        self.start = Button(self,text="Player " + str(self.turn) + "Start turn",command=self.begin,font=("Arial",30,"bold"))
        self.start.grid(row=5,column=6)


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
                self.start = Button(self, text="Player " + str(self.turn) + "Start turn", command=self.begin,
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

    def clear_board(self):
        if not self.cleared:
            if len(self.player1.p_hand) > 0:
                for x in range(len(self.player1.p_hand)):
                    self.player1.p_hand[x].destroy()
                for x in self.player1.p_hand:
                    self.player1.p_hand.remove(x)
            if len(self.player2.p_hand) > 0:
                for x in range(len(self.player2.p_hand)):
                    self.player2.p_hand[x].destroy()
                for x in self.player2.p_hand:
                    self.player2.p_hand.remove(x)
        else:
            self.cleared = True
        self.row = 5
        self.column = 1



    def stay(self):
        self.turn += 1
        self.clear_board()
        if self.turn < 3:
            if self.x:
                self.blackjack.destroy()
                self.x = False
            self.turn_switch(self.turn)
            self.start = Button(self, text="Player " + str(self.turn) + "Start turn", command=self.begin,
                                font=("Arial", 30, "bold"))
            self.start.grid(row=5, column=6)
            self.h.destroy()
            self.s.destroy()
        else:
            self.turn_switch(self.turn)
            self.h.destroy()
            self.s.destroy()


    def round_end(self):
        if self.player1.bust:
            if self.player2.bust:
                self.display_current = Label(self,text="Tie Round")
                self.display_current.grid(row=13,column=7,sticky=S)
                self.ties += 1
            else:
                self.display_current = Label(self,text="Player 2 Wins Round")
                self.display_current.grid(row=13,column=7,sticky=S)
                if self.rounds > self.player2.win + self.player1.win - self.ties:
                    self.player2.win += 1
        elif self.player2.bust:
            self.display_current = Label(self,text="PLayer 1 Wins Round")
            self.display_current.grid(row=13,column=7,sticky=S)
            if self.rounds > self.player1.win + self.player2.win - self.ties:
                self.player1.win += 1
        else:
            if self.player1.score > self.player2.score:
                self.display_current = Label(self,text="Player 1 Wins Round")
                self.display_current.grid(row=13,column=7,sticky=S)
                if self.rounds > self.player1.win + self.player2.win - self.ties:
                    self.player1.win += 1
            elif self.player2.score > self.player1.score:
                self.display_current = Label(self,text="Player 2 Wins Round")
                self.display_current.grid(row=13,column=7,sticky=S)
                if self.rounds > self.player1.win + self.player2.win - self.ties:
                    self.player2.win += 1
            else:
                self.display_current = Label(self,text="Tie Round")
                self.display_current.grid(row=13,column=7,sticky=S)
                self.ties += 1
        self.score_display()
        self.switch["text"] = None
        self.turn = 1
        self.cleared = False
        self.x = False
        self.player1.bust = False
        self.player2.bust = False
        self.end = True
        self.start = Button(self, text="Player " + str(self.turn) + "Start turn", command=self.begin,
                            font=("Arial", 30, "bold"))
        self.start.grid(row=5, column=6)

    def turn_switch(self,to):
        '''This method will display a constant label showing whose turn it is'''
        if self.turn < 3:
            self.switch = Label(self,text=("Turn: Player" + str(to)),font=("Times",16,"bold"))
            self.switch.grid(row=11,column=7,sticky=N)
        else:
            self.switch.destroy()
            self.switch = Label(self,text=("Round Over"),font=("Times",16,"bold"))
            self.switch.grid(row=11,column=7,sticky=N)
            self.round_end()




    def begin(self):
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
                self.blackjack = Button(self,text="Player 1 Blackjack",command=self.stay,font=("Arial",16,"bold"))
                self.blackjack.grid(row=2,column=4,rowspan=2,columnspan=3)
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
        self.start.destroy()
        self.h = Button(self,text="Hit",command=self.Hit)
        self.h.grid(row=2,column=14,sticky=E)
        self.s = Button(self,text="Stay",command=self.stay)
        self.s.grid(row=2,column=0,sticky=W)

    def score_display(self):
        self.p1_wins = Label(self,text=self.player1.win,font=("Times",12))
        self.p1_wins.grid(row=0,column=5,sticky=N)
        self.p2_wins = Label(self,text=self.player2.win,font=("Times",12))
        self.p2_wins.grid(row=0,column=8,sticky=N)

    def ace(self):
        self.h.destroy()
        self.s.destroy()
        self.valueButton = 0
        Button(text="I want my ace to be an 11", value=11, variable=self.valueButton).grid(row=2, column=14, sticky=E)
        Button(text="I want my ace to be a 1", value=1, variable=self.valueButton).grid(row=2, column=0, sticky=W)
        self.h = Button(self, text="Hit", command=self.Hit)
        self.h.grid(row=2, column=14, sticky=E)
        self.s = Button(self, text="Stay", command=self.stay)
        self.s.grid(row=2, column=0, sticky=W)