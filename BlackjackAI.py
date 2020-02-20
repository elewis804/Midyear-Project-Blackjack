from tkinter import *
from Blackjackinteractions import Player

class AIGame(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.row = 5
        self.column = 1
        self.rounds = 0
        self.player1 = Player()
        self.AIPlayer = Player()
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
        self.switch = Label(text="")
        self.start = Button(self,text="Player Start turn", bg = "indian red",font=("Arial",30,"bold"),command=self.begin)
        self.start.grid(row=5,column=6)


    def begin(self):
        self.start.destroy()
        self.switch["text"] = None
        for x in self.player1.hand:
            self.player1.hand.remove(x)
        self.player1.score = 0
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
        if self.x == False:
            self.h = Button(self,text="Hit",command=self.Hit)
            self.h.grid(row=2,column=14,sticky=E)
            self.s = Button(self,text="Stay",command=self.stay)
            self.s.grid(row=2,column=0,sticky=W)

    def Hit(self):
        if self.column >=4:
            self.row += 1
            self.column = 1
        if self.player1.score <= 20:
            self.player1.getRandomCard()
            self.player1.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand) - 1].image)
            self.player1.p_hand[len(self.player1.p_hand) - 1] = Label(self, image=card1)
            self.player1.p_hand[len(self.player1.p_hand) - 1].photo = card1
            self.player1.p_hand[len(self.player1.p_hand) - 1].grid(row=self.row, column=self.column)
            if self.player1.score > 21:
                self.player1.bust=TRUE
                self.h.destroy()
                self.s.destroy()
                self.clear_board()
                self.AI()
        elif self.player1.score > 21:
            self.player1.bust = TRUE
            self.h.destroy()
            self.s.destroy()
            self.clear_board()
            self.AI()




    def AI(self):
        self.AIPlayer.getRandomCard()
        self.AIPlayer.p_hand.append(0)
        self.AIPlayer.getRandomCard()
        self.AIPlayer.p_hand.append(0)
        while True:
            if self.AIPlayer.score >= 21:
                self.AIPlayer.bust = True
                self.round_end()
            elif self.AIPlayer.score >= 17:
                self.round_end()
            else:
                self.AIPlayer.getRandomCard()
                self.AIPlayer.p_hand.append(0)
    
    
    def stay(self):
        self.clear_board()
        self.AI()
    
    def clear_board(self):
        if not self.cleared:
            if 0 in self.player1.p_hand:
                self.player1.p_hand.remove(0)
            if len(self.player1.p_hand) > 0:
                for x in range(len(self.player1.p_hand)):
                    print(self.player1.p_hand[x])
                    self.player1.p_hand[x].destroy()
                for x in self.player1.p_hand:
                    self.player1.p_hand.remove(x)
            self.cleared = True
        else:
            self.cleared = True
        self.row = 5
        self.column = 1

    def score_display(self):
        self.p1_wins = Label(self, text="Player 1 wins: " + str(self.player1.win), bg="indian red",
                             font=("Times", 14))
        self.p1_wins.grid(row=0, column=5, sticky=N)
        self.p2_wins = Label(self, text="Player 2 wins:" + str(self.AIPlayer.win), bg="sky blue", font=("Times", 14))
        self.p2_wins.grid(row=0, column=8, sticky=N)
    def round_end(self):
        if self.player1.bust:
            if self.AIPlayer.bust:
                self.display_current = Label(self,text="Tie Round",bg="orchid2",font =14)
                self.display_current.grid(row=13,column=7,sticky=S)
                self.ties += 1
            else:
                self.display_current = Label(self,text="Player 2 Wins Round",bg="indian red")
                self.display_current.grid(row=13,column=7,sticky=S)
                if self.rounds > self.AIPlayer.win + self.player1.win - self.ties:
                    self.AIPlayer.win += 1
        elif self.AIPlayer.bust:
            self.display_current = Label(self,text="Player 1 Wins Round",bg="indian red")
            self.display_current.grid(row=13,column=7,sticky=S)
            if self.rounds > self.player1.win + self.AIPlayer.win - self.ties:
                self.player1.win += 1
        else:
            if self.player1.score > self.AIPlayer.score:
                self.display_current = Label(self,text="Player 1 Wins Round",bg="indian red")
                self.display_current.grid(row=13,column=7,sticky=S)
                if self.rounds > self.player1.win + self.AIPlayer.win - self.ties:
                    self.player1.win += 1
            elif self.AIPlayer.score > self.player1.score:
                self.display_current = Label(self,text="Player 2 Wins Round",bg="sky blue")
                self.display_current.grid(row=13,column=7,sticky=S)
                if self.rounds > self.player1.win + self.AIPlayer.win - self.ties:
                    self.AIPlayer.win += 1
            else:
                self.display_current = Label(self,text="Tie Round",bg ="orchid2")
                self.display_current.grid(row=13,column=7,sticky=S)
                self.ties += 1
        self.score_display()
        self.switch["text"] = None
        self.turn = 1
        self.cleared = False
        self.x = False
        self.player1.bust = False
        self.AIPlayer.bust = False
        self.end = True
        self.player1.score = 0
        self.AIPlayer.score = 0
        self.start = Button(self, text="Player " + str(self.turn)+" start turn",bg="indian red",command=self.begin,
                            font=("Arial", 30, "bold"))
        self.start.grid(row=5, column=6)