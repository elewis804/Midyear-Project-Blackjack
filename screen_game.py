from tkinter import *
from Blackjackinteractions import PlayerHand

class ScreenGame(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):


        Button(self,text="Hit",command=PlayerHand("Cards.txt").getRandomCard()).grid(row=3,column=3,sticky=E)
