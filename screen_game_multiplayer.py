from tkinter import *
from Blackjackinteractions import Player


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
        self.create_s_button()

    def create_s_button(self):
        self.start = Button(self, text="Player " + str(self.turn) + "Start turn", command=self.begin, bg="indian red",
                            font=("Arial", 30, "bold"))
        self.start.grid(row=5, column=6)


    def Hit(self):
        if self.turn == 1:
            self.player1.getRandomCard()
            if self.player1.score <= 21 and 0 not in self.player1.p_hand:
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
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player1.hand[len(self.player1.hand) - 1].image)
                    self.player1.p_hand[len(self.player1.p_hand) - 1] = Label(self, image=card1)
                    self.player1.p_hand[len(self.player1.p_hand) - 1].photo = card1
                    self.player1.p_hand[len(self.player1.p_hand) - 1].grid(row=self.row, column=self.column)
                    self.column += 1
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
            if self.player2.score <= 21 and 0 not in self.player2.p_hand:
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
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player2.hand[len(self.player2.hand) - 1].image)
                    self.player2.p_hand[len(self.player2.p_hand) - 1] = Label(self, image=card1)
                    self.player2.p_hand[len(self.player2.p_hand) - 1].photo = card1
                    self.player2.p_hand[len(self.player2.p_hand) - 1].grid(row=self.row, column=self.column)
                    self.column += 1
            else:
                self.turn = 3
                self.player2.bust = True
                self.clear_board()
                self.cleared = True
                self.turn_switch(self.turn)
                self.start = Button(self, text="Player " + str(self.turn) + " start turn", bg="yellow",
                                    command=self.begin,
                                    font=("Arial", 30, "bold"))
                self.start.grid(row=5, column=6)
                self.h.destroy()
                self.s.destroy()
                #possibly implement start button like is in player 1 bust

        elif self.turn == 3:
            self.player3.getRandomCard()
            if self.player3.score <= 21 and 0 not in self.player3.p_hand:
                self.player3.p_hand.append(0)
                if self.column < 4:
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player3.hand[len(self.player3.hand) - 1].image)
                    self.player3.p_hand[len(self.player3.p_hand) - 1] = Label(self, image=card1)
                    self.player3.p_hand[len(self.player3.p_hand) - 1].photo = card1
                    self.player3.p_hand[len(self.player3.p_hand) - 1].grid(row=self.row, column=self.column)
                    self.column += 1
                else:
                    self.row += 2
                    self.column = 1
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player3.hand[len(self.player3.hand) - 1].image)
                    self.player3.p_hand[len(self.player3.p_hand) - 1] = Label(self, image=card1)
                    self.player3.p_hand[len(self.player3.p_hand) - 1].photo = card1
                    self.player3.p_hand[len(self.player3.p_hand) - 1].grid(row=self.row, column=self.column)
                    self.column += 1
            else:
                self.turn = 4
                self.player3.bust = True
                self.clear_board()
                self.cleared = True
                self.turn_switch(self.turn)
                self.start = Button(self, text="Player " + str(self.turn) + " start turn", bg="magenta",
                                    command=self.begin,
                                    font=("Arial", 30, "bold"))
                self.start.grid(row=5, column=6)
                self.h.destroy()
                self.s.destroy()

        elif self.turn == 4:
            self.player4.getRandomCard()
            if self.player4.score <= 21 and 0 not in self.player4.p_hand:
                self.player4.p_hand.append(0)
                if self.column < 4:
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player4.hand[len(self.player4.hand) - 1].image)
                    self.player4.p_hand[len(self.player4.p_hand) - 1] = Label(self, image=card1)
                    self.player4.p_hand[len(self.player4.p_hand) - 1].photo = card1
                    self.player4.p_hand[len(self.player4.p_hand) - 1].grid(row=self.row, column=self.column)
                    self.column += 1
                else:
                    self.row += 2
                    self.column = 1
                    card1 = PhotoImage(file="Images-Blackjack/" + self.player4.hand[len(self.player4.hand) - 1].image)
                    self.player4.p_hand[len(self.player4.p_hand) - 1] = Label(self, image=card1)
                    self.player4.p_hand[len(self.player4.p_hand) - 1].photo = card1
                    self.player4.p_hand[len(self.player4.p_hand) - 1].grid(row=self.row, column=self.column)
                    self.column += 1
            else:
                self.turn = 5
                self.player4.bust = True
                self.clear_board()
                self.cleared = True
                self.turn_switch(self.turn)
                self.h.destroy()
                self.s.destroy()



    def clear_board(self):
        if not self.cleared:
            if 0 in self.player1.p_hand:
                while 0 in self.player1.p_hand:
                    self.player1.p_hand.remove(0)
            if 0 in self.player2.p_hand:
                while 0 in self.player2.p_hand:
                    self.player2.p_hand.remove(0)
            if 0 in self.player3.p_hand:
                while 0 in self.player3.p_hand:
                    self.player3.p_hand.remove(0)
            if 0 in self.player4.p_hand:
                while 0 in self.player4.p_hand:
                    self.player4.p_hand.remove(0)

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
            if len(self.player3.p_hand) > 0:
                for x in range(len(self.player3.p_hand)):
                    self.player3.p_hand[x].destroy()
                for x in self.player3.p_hand:
                    self.player3.p_hand.remove(x)
            if len(self.player4.p_hand) > 0:
                for x in range(len(self.player4.p_hand)):
                    self.player4.p_hand[x].destroy()
                for x in self.player4.p_hand:
                    self.player4.p_hand.remove(x)
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
        if self.turn < 5:
            self.turn_switch(self.turn)
            self.start = Button(self, text="Player " + str(self.turn) + "Start turn", command=self.begin,bg ="indian red",
                                font=("Arial", 30, "bold"))
            if self.turn == 2:
                self.start["bg"] = "sky blue"
            elif self.turn == 3:
                self.start["bg"] = "yellow"
            elif self.turn == 4:
                self.start["bg"] = "magenta"
            self.start.grid(row=5, column=6)
            self.h.destroy()
            self.s.destroy()
        else:
            self.turn_switch(self.turn)
            self.h.destroy()
            self.s.destroy()

    def round_end(self):
        self.winner()
        self.score_display()
        self.switch["text"] = None
        self.turn = 1
        self.cleared = False
        self.x = False
        self.player1.bust = False
        self.player2.bust = False
        self.player3.bust = False
        self.player4.bust = False
        self.end = True
        self.player1.score = 0
        self.player2.score = 0
        self.player3.score = 0
        self.player4.score = 0
        self.start = Button(self, text="Player " + str(self.turn)+" start turn",bg="indian red",command=self.begin,
                            font=("Arial", 30, "bold"))
        self.start.grid(row=5, column=6)

    def winner(self):
        p1b = self.player1.bust
        p2b = self.player2.bust
        p3b = self.player3.bust
        p4b = self.player4.bust



        if p1b:
            if p2b:
                if p3b:
                    if p4b:
                        self.display_current = Label(self, text="Tie Round", bg="orchid2", font=14)
                        self.display_current.grid(row=13, column=7, sticky=S)
                        self.ties += 1
                    else:
                        if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                            self.display_current = Label(self, text="Player 4 Wins", bg="orchid2", font=14)
                            self.display_current.grid(row=13, column=7, sticky=S)
                            self.player4.win += 1

                else:
                    if p4b:
                        if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 3 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player3.win += 1
                    else:
                        if self.player3.score > self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 3 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player3.win += 1

                        elif self.player3.score < self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 4 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player4.win += 1

                        else:
                            self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                            self.display_current.grid(row=13, column=7, sticky=S)
                            self.player3.win += 1
                            self.player4.win += 1
                            self.ties += 1
            else:
                if p4b:
                    if p3b:
                        if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                            self.display_current = Label(self, text="Player 2 Wins", bg="orchid2", font=14)
                            self.display_current.grid(row=13, column=7, sticky=S)
                            self.player2.win += 1

                    else:
                        if self.player2.score > self.player3.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 2 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player2.win += 1
                        elif self.player2.score < self.player3.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 3 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player3.win += 1
                        else:
                            self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                            self.display_current.grid(row=13, column=7, sticky=S)
                            self.player2.win += 1
                            self.player3.win += 1
                            self.ties += 1
                else:
                    if p3b:
                        if self.player2.score > self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 2 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player2.win += 1

                        elif self.player2.score < self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 4 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player4.win += 1

                        else:
                            self.display_current = Label(self, text="Tie Round", bg="orchid2", font=14)
                            self.display_current.grid(row=13, column=7, sticky=S)
                            self.ties += 1
                    else:
                        if self.player2.score > self.player3.score and self.player2.score > self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 2 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player2.win += 1

                        elif self.player3.score > self.player2.score and self.player3.score > self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 3 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player3.win += 1

                        elif self.player4.score > self.player3.score and self.player4.score > self.player2.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 4 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player4.win += 1

                        elif self.player2.score == self.player3.score and self.player2.score > self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player2.win += 1
                                self.player3.win += 1
                                self.ties += 1
                        elif self.player2.score == self.player4.score and self.player2.score  > self.player3.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player2.win += 1
                                self.player4.win += 1
                                self.ties += 1
                        elif self.player3.score == self.player4.score and self.player3.score > self.player2.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player4.win += 1
                                self.player3.win += 1
                                self.ties += 1
                        elif self.player2.score == self.player3.score and self.player2.score == self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player2.win += 1
                                self.player3.win += 1
                                self.player4.win += 1
                                self.ties += 2
        else:
            if p2b:
                if p3b:
                    if p4b:
                        if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                            self.display_current = Label(self, text="Player 1 Wins", bg="orchid2", font=14)
                            self.display_current.grid(row=13, column=7, sticky=S)
                            self.player1.win += 1
                    else:
                        if self.player1.score > self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 1 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player1.win += 1
                        elif self.player1.score < self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 4 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player4.win += 1

                        else:
                            self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                            self.display_current.grid(row=13, column=7, sticky=S)
                            self.player1.win += 1
                            self.player4.win += 1
                            self.ties += 1
                else:
                    if p4b:
                        if self.player1.score > self.player3.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 1 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player1.win += 1
                        elif self.player1.score < self.player3.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 3 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player3.win += 1
                        else:
                            self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                            self.display_current.grid(row=13, column=7, sticky=S)
                            self.player1.win += 1
                            self.player3.win += 1
                            self.ties += 1
                    else:
                        if self.player1.score > self.player3.score and self.player1.score > self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 1 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player1.win += 1

                        elif self.player3.score > self.player1.score and self.player3.score > self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 3 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player3.win += 1

                        elif self.player4.score > self.player3.score and self.player4.score > self.player1.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 4 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player4.win += 1

                        elif self.player1.score == self.player3.score and self.player1.score > self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player1.win += 1
                                self.player3.win += 1
                                self.ties += 1
                        elif self.player1.score == self.player4.score and self.player1.score  > self.player3.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player1.win += 1
                                self.player4.win += 1
                                self.ties += 1
                        elif self.player3.score == self.player4.score and self.player3.score > self.player1.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player4.win += 1
                                self.player3.win += 1
                                self.ties += 1
                        elif self.player1.score == self.player3.score and self.player1.score == self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player1.win += 1
                                self.player3.win += 1
                                self.player4.win += 1
                                self.ties += 2
            else:
                if p3b:
                    if p4b:
                        if self.player1.score > self.player2.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 1 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player1.win += 1
                        elif self.player1.score < self.player2.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 2 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player2.win += 1
                        else:
                            self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                            self.display_current.grid(row=13, column=7, sticky=S)
                            self.player1.win += 1
                            self.player2.win += 1
                            self.ties += 1
                    else:
                        if self.player1.score > self.player4.score and self.player1.score > self.player2.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 1 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player1.win += 1

                        elif self.player4.score > self.player1.score and self.player4.score > self.player2.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 4 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player4.win += 1

                        elif self.player2.score > self.player4.score and self.player2.score > self.player1.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 2 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player2.win += 1

                        elif self.player1.score == self.player4.score and self.player1.score > self.player2.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player1.win += 1
                                self.player4.win += 1
                                self.ties += 1
                        elif self.player1.score == self.player2.score and self.player1.score  > self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player1.win += 1
                                self.player2.win += 1
                                self.ties += 1
                        elif self.player4.score == self.player2.score and self.player4.score > self.player1.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player2.win += 1
                                self.player4.win += 1
                                self.ties += 1
                        elif self.player1.score == self.player4.score and self.player1.score == self.player2.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player1.win += 1
                                self.player4.win += 1
                                self.player2.win += 1
                                self.ties += 2
                else:
                    if p4b:
                        if self.player2.score > self.player3.score and self.player2.score > self.player1.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 2 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player2.win += 1

                        elif self.player3.score > self.player2.score and self.player3.score > self.player1.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 3 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player3.win += 1

                        elif self.player1.score > self.player3.score and self.player1.score > self.player2.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 1 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player1.win += 1

                        elif self.player2.score == self.player3.score and self.player2.score > self.player1.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player2.win += 1
                                self.player3.win += 1
                                self.ties += 1
                        elif self.player2.score == self.player1.score and self.player2.score  > self.player3.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player2.win += 1
                                self.player1.win += 1
                                self.ties += 1
                        elif self.player3.score == self.player1.score and self.player3.score > self.player2.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player1.win += 1
                                self.player3.win += 1
                                self.ties += 1
                        elif self.player2.score == self.player3.score and self.player2.score == self.player1.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player2.win += 1
                                self.player3.win += 1
                                self.player1.win += 1
                                self.ties += 2
                    else:
                        if self.player1.score > self.player2.score and self.player1.score > self.player3.score and self.player1.score > self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 1 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player1.win += 1
                        elif self.player2.score > self.player1.score and self.player2.score > self.player3.score and self.player2.score > self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 2 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player2.win += 1
                        elif self.player3.score > self.player1.score and self.player3.score > self.player2.score and self.player3.score > self.player4.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 3 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player3.win += 1
                        elif self.player4.score > self.player1.score and self.player4.score > self.player2.score and self.player4.score > self.player3.score:
                            if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                self.display_current = Label(self, text="Player 4 Wins", bg="orchid2", font=14)
                                self.display_current.grid(row=13, column=7, sticky=S)
                                self.player4.win += 1
                        elif self.player1.score == self.player2.score:
                            if self.player1.score > self.player3.score and self.player1.score > self.player4.score:
                                if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                    self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                    self.display_current.grid(row=13, column=7, sticky=S)
                                    self.player1.win += 1
                                    self.player2.win += 1
                                    self.ties += 1
                            elif self.player1.score == self.player3.score and self.player1.score > self.player4.score:
                                if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                    self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                    self.display_current.grid(row=13, column=7, sticky=S)
                                    self.player1.win += 1
                                    self.player2.win += 1
                                    self.player3.win += 1
                                    self.ties += 2
                            elif self.player1.score == self.player4.score and self.player1.score > self.player3.score:
                                if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                    self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                    self.display_current.grid(row=13, column=7, sticky=S)
                                    self.player1.win += 1
                                    self.player2.win += 1
                                    self.player4.win += 1
                                    self.ties += 2
                            elif self.player1.score == self.player3.score and self.player1.score == self.player4.score:
                                if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                    self.display_current = Label(self, text="Tie Round", bg="orchid2", font=14)
                                    self.display_current.grid(row=13, column=7, sticky=S)
                                    self.player1.win += 1
                                    self.player2.win += 1
                                    self.player3.win += 1
                                    self.player4.win += 1
                                    self.ties += 3
                        elif self.player1.score == self.player3.score:
                            if self.player1.score > self.player2.score and self.player1.score > self.player4.score:
                                if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                    self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                    self.display_current.grid(row=13, column=7, sticky=S)
                                    self.player1.win += 1
                                    self.player3.win += 1
                                    self.ties += 1
                            elif self.player1.score == self.player4.score and self.player1.score > self.player2.score:
                                if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                    self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                    self.display_current.grid(row=13, column=7, sticky=S)
                                    self.player1.win += 1
                                    self.player3.win += 1
                                    self.player4.win += 1
                                    self.ties += 2
                        elif self.player1.score == self.player4.score:
                            if self.player4.score > self.player3.score and self.player4.score > self.player2.score:
                                if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                    self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                    self.display_current.grid(row=13, column=7, sticky=S)
                                    self.player1.win += 1
                                    self.player4.win += 1
                                    self.ties += 1
                        elif self.player2.score == self.player3.score:
                            if self.player2.score > self.player1.score and self.player2.score > self.player4.score:
                                if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                    self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                    self.display_current.grid(row=13, column=7, sticky=S)
                                    self.player2.win += 1
                                    self.player3.win += 1
                                    self.ties += 1
                            elif self.player2.score == self.player4.score and self.player2.score > self.player1.score:
                                if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                    self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                    self.display_current.grid(row=13, column=7, sticky=S)
                                    self.player2.win += 1
                                    self.player3.win += 1
                                    self.player4.win+= 1
                                    self.ties += 2
                        elif self.player2.score == self.player4.score:
                            if self.player2.score > self.player1.score and self.player2.score > self.player3.score:
                                if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                    self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                    self.display_current.grid(row=13, column=7, sticky=S)
                                    self.player2.win += 1
                                    self.player4.win += 1
                                    self.ties += 1
                        elif self.player3.score == self.player4.score:
                            if self.player3.score > self.player1.score and self.player3.score > self.player2.score:
                                if self.rounds > self.player2.win + self.player1.win + self.player3.win + self.player4.win - self.ties:
                                    self.display_current = Label(self, text="Multi Win", bg="orchid2", font=14)
                                    self.display_current.grid(row=13, column=7, sticky=S)
                                    self.player3.win += 1
                                    self.player4.win += 1
                                    self.ties += 1


    def turn_switch(self,to):
        '''This method will display a constant label showing whose turn it is'''
        if self.turn < 5:
            self.switch = Label(self,text=("Turn: Player" + str(to)),font=("Times",16,"bold"))
            self.switch.grid(row=11,column=7,sticky=N)
        else:
            self.switch.destroy()
            self.switch = Label(self,text=("Round Over"),font=("Times",16,"bold"))
            self.switch.grid(row=11,column=7,sticky=N)
            self.round_end()

    def begin(self):
        if self.rounds > 1:
            if self.turn == 1:
                self.switch["text"] = None
        if self.turn == 1:
            self.switch = Label(self, text=("Turn: Player " + str(self.turn)), font=("Times",16))
            self.switch.grid(row=11, column=7, sticky=N)
            self.rounds += 1
            for f in self.player1.hand:
                self.player1.hand.remove(f)
            for h in self.player2.hand:
                self.player2.hand.remove(h)
            self.player1.score = 0
            self.player2.score = 0
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
            if self.player1.score == 21:
                self.x = True
                self.blackjack = Button(self,text="Player 1 Blackjack",bg="indian red",command=self.stay,font=("Arial",16,"bold"))
                self.blackjack.grid(row=2,column=4,rowspan=2,columnspan=6)

        elif self.turn == 2:
            if not self.cleared:
                self.clear_board()
            else:
                self.cleared = False
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
            if self.player2.score == 21:
                self.x = True
                self.blackjack = Button(self,text="Player 2 Blackjack",bg="sky blue",command=self.stay,font=("Arial",16,"bold"))
                self.blackjack.grid(row=2,column=4,rowspan=2,columnspan=6)

        elif self.turn == 3:
            if not self.cleared:
                self.clear_board()
            else:
                self.cleared = False
            self.player3.clear_hand()
            self.player3.getRandomCard(True)
            self.player3.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player3.hand[len(self.player3.hand) - 1].image)
            self.player3.p_hand[len(self.player3.p_hand) - 1] = Label(self, image=card1)
            self.player3.p_hand[len(self.player3.p_hand) - 1].photo = card1
            self.player3.p_hand[len(self.player3.p_hand) - 1].grid(row=self.row, column=self.column)
            self.column += 1
            self.player3.getRandomCard(True)
            self.player3.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player3.hand[len(self.player3.hand) - 1].image)
            self.player3.p_hand[len(self.player3.p_hand) - 1] = Label(self, image=card1)
            self.player3.p_hand[len(self.player3.p_hand) - 1].photo = card1
            self.player3.p_hand[len(self.player3.p_hand) - 1].grid(row=self.row, column=self.column)
            self.column += 1
            if self.player3.score == 21:
                self.x = True
                self.blackjack = Button(self,text="Player 3 Blackjack",bg="yellow",command=self.stay,font=("Arial",16,"bold"))
                self.blackjack.grid(row=2,column=4,rowspan=2,columnspan=6)

        elif self.turn == 4:
            if not self.cleared:
                self.clear_board()
            else:
                self.cleared = False
            self.player4.clear_hand()
            self.player4.getRandomCard(True)
            self.player4.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player4.hand[len(self.player4.hand) - 1].image)
            self.player4.p_hand[len(self.player4.p_hand) - 1] = Label(self, image=card1)
            self.player4.p_hand[len(self.player4.p_hand) - 1].photo = card1
            self.player4.p_hand[len(self.player4.p_hand) - 1].grid(row=self.row, column=self.column)
            self.column += 1
            self.player4.getRandomCard(True)
            self.player4.p_hand.append(0)
            card1 = PhotoImage(file="Images-Blackjack/" + self.player4.hand[len(self.player4.hand) - 1].image)
            self.player4.p_hand[len(self.player4.p_hand) - 1] = Label(self, image=card1)
            self.player4.p_hand[len(self.player4.p_hand) - 1].photo = card1
            self.player4.p_hand[len(self.player4.p_hand) - 1].grid(row=self.row, column=self.column)
            self.column += 1
            if self.player4.score == 21:
                self.x = True
                self.blackjack = Button(self,text="Player 4 Blackjack",bg="magenta",command=self.stay,font=("Arial",16,"bold"))
                self.blackjack.grid(row=2,column=4,rowspan=2,columnspan=6)
        self.start.destroy()
        if not self.x:
            self.h = Button(self,text="Hit",command=self.Hit)
            self.h.grid(row=2,column=14,sticky=E)
            self.s = Button(self,text="Stay",command=self.stay)
            self.s.grid(row=2,column=0,sticky=W)

    def score_display(self):
        self.p1_wins = Label(self,text="Player 1 wins: "+str(self.player1.win),bg="indian red",font=("Times",14))
        self.p1_wins.grid(row=0,column=3,sticky=N)

        self.p2_wins = Label(self,text="Player 2 wins:"+str(self.player2.win),bg="sky blue",font=("Times",14))
        self.p2_wins.grid(row=0,column=5,sticky=N)

        self.p3_wins = Label(self, text="Player 3 wins:" + str(self.player3.win), bg="yellow", font=("Times", 14))
        self.p3_wins.grid(row=0, column=7, sticky=N)

        self.p4_wins = Label(self, text="Player 4 wins:" + str(self.player4.win), bg="magenta", font=("Times", 14))
        self.p4_wins.grid(row=0, column=9, sticky=N)

