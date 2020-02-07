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
        if self.player1.score <= 20:
            self.player1.getRandomCard()
            self.player1.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand) - 1].image)
            self.player1.p_hand[len(self.player1.p_hand) - 1] = Label(self, image=card1)
            self.player1.p_hand[len(self.player1.p_hand) - 1].photo = card1
            self.player1.p_hand[len(self.player1.p_hand) - 1].grid(row=self.row, column=self.column)
        elif self.player1.score > 21:
            self.player1.bust=TRUE
            self.AI()



    def AI(self):
        self.AIPlayer.getRandomCard()
        self.AIPlayer.p_hand.append(0)
        self.AIPlayer.getRandomCard()
        self.AIPlayer.p_hand.append(0)
        if self.AIPlayer.score == 21 and self.x==FALSE:
            print("AI Wins")
        elif self.AIPlayer.score >= 17:
            print("Will compare the cards of player and AI")
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
