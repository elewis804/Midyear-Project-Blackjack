from tkinter import *
from StartScreen import Start

class Screen_Manager(object):
    def __init__(self):
        self.root=Tk()
        self.currentScreen=None

    def start_screen(self):
        self.root.title("Start the Game!")
        self.currentScreen=StartScreen.Start(self.root)
