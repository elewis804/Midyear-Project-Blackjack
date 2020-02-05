from tkinter import *
from StartScreen import Start
from screen_game import ScreenGame
from BlackjackAI import AIGame


class Screen_Manager(object):
    def __init__(self):
        self.root = Tk()
        self.currentScreen = None

    def start_screen(self):
        self.root.title("Main Menu")
        self.currentScreen = Start(self.root, self.startup_screengame, self.startup_AIGame)


    def startup_screengame(self):
        self.currentScreen.destroy()
        self.root.title("BlackJack!")
        self.currentScreen = ScreenGame(self.root)
    
    def startup_AIGame(self):
        self.currentScreen.destroy()
        self.root.title("Blackjack!")
        self.currentScreen = AIGame(self.root)

def main():
    game = Screen_Manager()
    game.start_screen()
    game.root.mainloop()


main()
