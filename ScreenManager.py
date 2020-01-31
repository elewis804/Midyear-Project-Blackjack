from tkinter import *
from StartScreen import Start
from screen_game import ScreenGame

class Screen_Manager(object):
    def __init__(self):
        self.root = Tk()
        self.currentScreen = None

    def start_screen(self):
        self.root.title("Start the Game!")
        self.currentScreen = Start(self.root, self.next_screen())

    def next_screen(self):
        self.currentScreen=ScreenGame(self.root)


def main():
    game = Screen_Manager()
    game.start_screen()
    game.root.mainloop()

main()
