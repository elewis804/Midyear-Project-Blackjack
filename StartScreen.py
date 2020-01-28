from tkinter import *
class Application(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
      Label(text = "Welcome to Blackjack!",fg = "green",font = 31).grid(row = 0,column = 0,sticky = N)
      Label(text = "Made by 
      Button(text = "Begin!",bg = "green",command= self.startgame).grid(row = 2,column = 0,sticky = N )
    def startgame(self):
root = Tk()
root.title("BlackJack")
app = Application(root)
root.mainloop()
