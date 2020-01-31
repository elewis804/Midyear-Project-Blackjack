from tkinter import *
from StartScreen import Start
<<<<<<< HEAD
=======

>>>>>>> 97d3d2f5aa30458ba0422238438161cb8f4d26c4

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
<<<<<<< HEAD
=======

        self.currentScreen=Start(self.root)
>>>>>>> 97d3d2f5aa30458ba0422238438161cb8f4d26c4
