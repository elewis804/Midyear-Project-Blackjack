from tkinter import *
import time
from Blackjackinteractions import Player

'''TO DO:
Screen Game is currently hard coded to be fixated on turns of only two players. If this is to be fixed, the easiest 
solution would likely be changing any part of the code that relies on self.turn being < 3 to being < the number of 
players, which can be added as an additional attribute of init. Obviously, the goal is to only have up to 4 players,
but hard coding two more players would likely take more time than just allowing for a potentially infinite amount. 
Additionally, Interactions will need to have a way to end the game and display final scores if the deck of cards gets
down to 1, or a way to refill each player's hand once they drop to a certain point. 
'''
class ScreenGameMultiplayer(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.row = 5
        self.column = 1
        self.rounds = 0
        self.player1 = Player()
        self.player2 = Player()
        self.player3 = Player()
        self.player4 = Player()
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
        self.get_num_players()

    def create_s_button(self):
        self.maxturns = self.players.get()
        self.start = Button(self, text="Player " + str(self.turn) + "Start turn", command=self.begin, bg="indian red",
                            font=("Arial", 30, "bold"))
        self.start.grid(row=5, column=6)

    def get_num_players(self):
        self.players = IntVar()
        self.players.set(None)
        Radiobutton(self,text="Two Players",value=2,variable=self.players).grid(row=5,column=4,sticky=W)
        Radiobutton(self,text="Three Players",value=3,variable=self.players).grid(row=6,column=4,sitcky=W)
        Radiobutton(self,text="Four Players",value=4,variable=self.players).grid(row=7,column=4,sticky=W)
        Button(self,text="Start",command=self.create_s_button).grid(row=9,column=6,sticky=S)




    def Hit(self):
        if self.turn == 1:
            self.player1.getRandomCard()
            if self.player1.score <= 21 and 0 not in self.player1.p_hand:
                self.player1.p_hand.append(0)
                print("Scores after p1 hit without bust (beg):")
                print("Player 1 score:", self.player1.score)
                print("Player 2 score:", self.player2.score)
                if self.column < 4:
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand) - 1].image)
                    self.player1.p_hand[len(self.player1.p_hand) - 1] = Label(self, image=card1)
                    self.player1.p_hand[len(self.player1.p_hand) - 1].photo = card1
                    self.player1.p_hand[len(self.player1.p_hand) - 1].grid(row=self.row, column=self.column)
                    self.column += 1
                else:
                    self.row += 2
                    self.column = 1
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand) - 1].image)
                    self.player1.p_hand[len(self.player1.p_hand) - 1] = Label(self, image=card1)
                    self.player1.p_hand[len(self.player1.p_hand) - 1].photo = card1
                    self.player1.p_hand[len(self.player1.p_hand) - 1].grid(row=self.row, column=self.column)
                    self.column += 1
                print("Scores after p1 hit without bust (end):")
                print("Player 1 score:", self.player1.score)
                print("Player 2 score:", self.player2.score)
            else:
                print("Scores after p1 hit with bust (beg):")
                print("Player 1 score:", self.player1.score)
                print("Player 2 score:", self.player2.score)
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
                print("Scores after p1 hit with bust (end):")
                print("Player 1 score:", self.player1.score)
                print("Player 2 score:", self.player2.score)

        elif self.turn == 2:
            self.player2.getRandomCard()
            if self.player2.score <= 21 and 0 not in self.player2.p_hand:
                self.player2.p_hand.append(0)
                print("Scores after p2 hit without bust(beg):")
                print("Player 1 score:", self.player1.score)
                print("Player 2 score:", self.player2.score)
                if self.column < 4:
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player2.hand[len(self.player2.hand) - 1].image)
                    self.player2.p_hand[len(self.player2.p_hand) - 1] = Label(self, image=card1)
                    self.player2.p_hand[len(self.player2.p_hand) - 1].photo = card1
                    self.player2.p_hand[len(self.player2.p_hand) - 1].grid(row=self.row, column=self.column)
                    self.column += 1
                else:
                    self.row += 2
                    self.column = 1
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player2.hand[len(self.player2.hand) - 1].image)
                    self.player2.p_hand[len(self.player2.p_hand) - 1] = Label(self, image=card1)
                    self.player2.p_hand[len(self.player2.p_hand) - 1].photo = card1
                    self.player2.p_hand[len(self.player2.p_hand) - 1].grid(row=self.row, column=self.column)
                    self.column += 1
                print("Scores after p1 hit without bust(end):")
                print("Player 1 score:", self.player1.score)
                print("Player 2 score:", self.player2.score)
            else:
                print("Scores after p2 hit with bust(beg):")
                print("Player 1 score:", self.player1.score)
                print("Player 2 score:", self.player2.score)
                self.turn = 3
                self.player2.bust = True
                self.clear_board()
                self.cleared = True
                self.turn_switch(self.turn)
                self.h.destroy()
                self.s.destroy()


        elif self.turn == 2:
            self.player2.getRandomCard()
            if self.player2.score <= 21 and 0 not in self.player2.p_hand:
                self.player2.p_hand.append(0)
                print("Scores after p2 hit without bust(beg):")
                print("Player 1 score:", self.player1.score)
                print("Player 2 score:", self.player2.score)
                if self.column < 4:
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player2.hand[len(self.player2.hand) - 1].image)
                    self.player2.p_hand[len(self.player2.p_hand) - 1] = Label(self, image=card1)
                    self.player2.p_hand[len(self.player2.p_hand) - 1].photo = card1
                    self.player2.p_hand[len(self.player2.p_hand) - 1].grid(row=self.row, column=self.column)
                    self.column += 1
                else:
                    self.row += 2
                    self.column = 1
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player2.hand[len(self.player2.hand) - 1].image)
                    self.player2.p_hand[len(self.player2.p_hand) - 1] = Label(self, image=card1)
                    self.player2.p_hand[len(self.player2.p_hand) - 1].photo = card1
                    self.player2.p_hand[len(self.player2.p_hand) - 1].grid(row=self.row, column=self.column)
                    self.column += 1
                print("Scores after p1 hit without bust(end):")
                print("Player 1 score:", self.player1.score)
                print("Player 2 score:", self.player2.score)
            else:
                print("Scores after p2 hit with bust(beg):")
                print("Player 1 score:", self.player1.score)
                print("Player 2 score:", self.player2.score)
                self.turn = 3
                self.player2.bust = True
                self.clear_board()
                self.cleared = True
                self.turn_switch(self.turn)
                self.h.destroy()
                self.s.destroy()
                print("Scores after p2 hit with bust(end):")
                print("Player 1 score:", self.player1.score)
                print("Player 2 score:", self.player2.score)

    def clear_board(self):
        if not self.cleared:
            if 0 in self.player1.p_hand:
                while 0 in self.player1.p_hand:
                    self.player1.p_hand.remove(0)
            if 0 in self.player2.p_hand:
                while 0 in self.player2.p_hand:
                    self.player2.p_hand.remove(0)

            if len(self.player1.p_hand) > 0:
                for x in range(len(self.player1.p_hand)):
                    print(self.player1.p_hand[x])
                    self.player1.p_hand[x].destroy()
                for x in self.player1.p_hand:
                    self.player1.p_hand.remove(x)
            if len(self.player2.p_hand) > 0:
                for x in range(len(self.player2.p_hand)):
                    self.player2.p_hand[x].destroy()
                for x in self.player2.p_hand:
                    self.player2.p_hand.remove(x)
            self.cleared = True
        else:
            self.cleared = True
        self.row = 5
        self.column = 1



    def stay(self):
        self.turn += 1
        self.clear_board()
        if self.x:
            self.x = False
            self.blackjack.destroy()
        if self.turn < 3:
            self.turn_switch(self.turn)
            self.start = Button(self, text="Player " + str(self.turn) + "Start turn", command=self.begin,bg ="indian red",
                                font=("Arial", 30, "bold"))
            if self.turn == 2:
                self.start["bg"] = "sky blue"
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
                self.display_current = Label(self,text="Tie Round",bg="orchid2",font =14)
                self.display_current.grid(row=13,column=7,sticky=S)
                self.ties += 1
            else:
                self.display_current = Label(self,text="Player 2 Wins Round",bg="indian red")
                self.display_current.grid(row=13,column=7,sticky=S)
                if self.rounds > self.player2.win + self.player1.win - self.ties:
                    self.player2.win += 1
        elif self.player2.bust:
            self.display_current = Label(self,text="Player 1 Wins Round",bg="indian red")
            self.display_current.grid(row=13,column=7,sticky=S)
            if self.rounds > self.player1.win + self.player2.win - self.ties:
                self.player1.win += 1
        else:
            if self.player1.score > self.player2.score:
                self.display_current = Label(self,text="Player 1 Wins Round",bg="indian red")
                self.display_current.grid(row=13,column=7,sticky=S)
                if self.rounds > self.player1.win + self.player2.win - self.ties:
                    self.player1.win += 1
            elif self.player2.score > self.player1.score:
                self.display_current = Label(self,text="Player 2 Wins Round",bg="sky blue")
                self.display_current.grid(row=13,column=7,sticky=S)
                if self.rounds > self.player1.win + self.player2.win - self.ties:
                    self.player2.win += 1
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
        self.player2.bust = False
        self.end = True
        self.player1.score = 0
        self.player2.score = 0
        self.start = Button(self, text="Player " + str(self.turn)+" start turn",bg="indian red",command=self.begin,
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
        print("Scores before begin:")
        print("Player 1 score:", self.player1.score)
        print("Player 2 score:", self.player2.score)
        if self.rounds > 1:
            if self.turn == 1:
                self.switch["text"] = None
        if self.turn == 1:
            self.rounds += 1
            for f in self.player1.hand:
                self.player1.hand.remove(f)
            for h in self.player2.hand:
                self.player2.hand.remove(h)
            self.player1.score = 0
            self.player2.score = 0
            print("Scores before begin for player 1:")
            print("Player 1 score:", self.player1.score)
            print("Player 2 score:", self.player2.score)
        if self.rounds > 1:
            self.display_current.destroy()
        if self.turn == 1:
            self.player1.clear_hand()
            self.player1.getRandomCard(True)
            self.player1.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand) - 1].image)
            self.player1.p_hand[len(self.player1.p_hand) - 1] = Label(self, image=card1)
            self.player1.p_hand[len(self.player1.p_hand) - 1].photo = card1
            self.player1.p_hand[len(self.player1.p_hand) - 1].grid(row=self.row, column=self.column)
            self.column += 1
            self.player1.getRandomCard(True)
            self.player1.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand) - 1].image)
            self.player1.p_hand[len(self.player1.p_hand) - 1] = Label(self, image=card1)
            self.player1.p_hand[len(self.player1.p_hand) - 1].photo = card1
            self.player1.p_hand[len(self.player1.p_hand) - 1].grid(row=self.row, column=self.column)
            self.column += 1
            print("Scores after p1 begin:")
            print("Player 1 score:", self.player1.score)
            print("Player 2 score:", self.player2.score)
            if self.player1.score == 21:
                self.x = True
                self.blackjack = Button(self,text="Player 1 Blackjack",bg="indian red",command=self.stay,font=("Arial",16,"bold"))
                self.blackjack.grid(row=2,column=4,rowspan=2,columnspan=6)
                print("Scores after p1 blackjack:")
                print("Player 1 score:", self.player1.score)
                print("Player 2 score:", self.player2.score)
        elif self.turn == 2:
            if not self.cleared:
                self.clear_board()
            else:
                self.cleared = False
            print("Scores before p2 begin:")
            print("Player 1 score:", self.player1.score)
            print("Player 2 score:", self.player2.score)
            self.player2.clear_hand()
            self.player2.getRandomCard(True)
            self.player2.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player2.hand[len(self.player2.hand) - 1].image)
            self.player2.p_hand[len(self.player2.p_hand) - 1] = Label(self, image=card1)
            self.player2.p_hand[len(self.player2.p_hand) - 1].photo = card1
            self.player2.p_hand[len(self.player2.p_hand) - 1].grid(row=self.row, column=self.column)
            self.column += 1
            self.player2.getRandomCard(True)
            self.player2.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player2.hand[len(self.player2.hand) - 1].image)
            self.player2.p_hand[len(self.player2.p_hand) - 1] = Label(self, image=card1)
            self.player2.p_hand[len(self.player2.p_hand) - 1].photo = card1
            self.player2.p_hand[len(self.player2.p_hand) - 1].grid(row=self.row, column=self.column)
            self.column += 1
            print("Scores after p2 begin:")
            print("Player 1 score:", self.player1.score)
            print("Player 2 score:", self.player2.score)
            if self.player2.score == 21:
                self.x = True
                self.blackjack = Button(self,text="Player 2 Blackjack",bg="sky blue",command=self.stay,font=("Arial",16,"bold"))
                self.blackjack.grid(row=2,column=4,rowspan=2,columnspan=6)
                print("Scores after p2 blackjack:")
                print("Player 1 score:", self.player1.score)
                print("Player 2 score:", self.player2.score)
        self.start.destroy()
        if not self.x:
            self.h = Button(self,text="Hit",command=self.Hit)
            self.h.grid(row=2,column=14,sticky=E)
            self.s = Button(self,text="Stay",command=self.stay)
            self.s.grid(row=2,column=0,sticky=W)

    def score_display(self):
        self.p1_wins = Label(self,text="Player 1 wins: "+str(self.player1.win),bg="indian red",font=("Times",14))
        self.p1_wins.grid(row=0,column=5,sticky=N)
        self.p2_wins = Label(self,text="Player 2 wins:"+str(self.player2.win),bg="sky blue",font=("Times",14))
        self.p2_wins.grid(row=0,column=8,sticky=N)
