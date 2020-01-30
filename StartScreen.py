from tkinter import *

from ScreenManager import Screen_Manager

class Start(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
      Label(self,text="Welcome to Blackjack!",fg = "green",font = 31).grid(row = 0,column = 0,sticky = N)
      Label(self,text="Made by Benen  -  Erik  -  Hayun  -  Lukas").grid(row=1,column=0,sticky=N)
      Button(self,text="Begin!",bg = "green",command= self.startgame).grid(row = 2,column = 0,sticky = N )

    def startgame(self):
        Screen_Manager.start()


