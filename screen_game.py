from tkinter import *
import time
from Blackjackinteractions import Player

class ScreenGame(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.player1 = Player()
        self.player2 = Player()
        self.turn = 1
        self.grid()
        self.create_widgets()

    def create_widgets(self):


        Button(self,text="Hit",command=self.Hit).grid(row=3,column=3,sticky=E)


    def Hit(self):
        if self.turn == 1:
            if self.player1.score <= 20:
                self.player1.getRandomCard()
            else:
                self.turn = 2
                self.turn_switch("Two")
        elif self.turn == 2:
            if self.player2.score <= 20:
                self.player2.getRandomCard()
            else:
                self.turn = 1
                self.turn_switch("One")


    def turn_switch(self,to):
        '''This method will display a temporary label using time to show the turn has swtiched'''
        Label(self,text=("Turn Switch to player", to),font=18).grid(row=0,column=1,sticky=N)


