from tkinter import *



class Start(Frame):
    def __init__(self, master, close_file):
        super(Start, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.close_file = close_file

    def create_widgets(self):
<<<<<<< HEAD
        Label(self, text="Welcome to Blackjack!", fg="green", font=31).grid(row=0, column=0, sticky=N)
        Label(self, text="Made by").grid(row=1, column=0, sticky=N)
        Button(self, text="Begin!", bg="green", command=self.startgame).grid(row=2, column=0, sticky=N)

    def startgame(self):
        self.close_file()
=======
      Label(self,text="Welcome to Blackjack!",fg = "green",font = 31).grid(row = 0,column = 0,sticky = N)
      Label(self,text="Made by Benen  -  Erik  -  Hayun  -  Lukas").grid(row=1,column=0,sticky=N)
      Button(self,text="Begin!",bg = "green",command= self.startgame).grid(row = 2,column = 0,sticky = N )

    def startgame(self):
        Screen_Manager.start()

>>>>>>> 3ddd6df9f9c66eef9807f68b370e3ccec47d240e

