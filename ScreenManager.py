from tkinter import *
from StartScreen import Start
<<<<<<< HEAD
=======

>>>>>>> dd2c761463a0cc4435617c8f149734fad832668f

class Screen_Manager(object):
    def __init__(self):
        self.root = Tk()
        self.currentScreen = None

    def start_screen(self):
        self.root.title("Start the Game!")
        self.currentScreen = Start(self.root, self.next_screen())

    def next_screen(self):
        print("Hi")


def main():
    game = Screen_Manager()
    game.start_screen()
    game.root.mainloop()

main()
