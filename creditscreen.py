from tkinter import *

class Credit(Frame):
    def __init__(self, master,closefile):
        super(Credit, self).__init__(master)
        self.closefile = closefile
        self.grid()
        quill = PhotoImage(file="Images-Blackjack/creditscreen.png")
        q = Label(self, image=quill)
        q.photo = quill
        q.grid(row=0, column=0, rowspan=15, columnspan=15)
        self.create_widgets()


    def create_widgets(self):
        Label(self, text = "    Made by Benen Sullivan, Lukas Tegge, Hayun Jung, and Eric Lewis  ", bg = 'gold', font = ("Arial",19, "bold")).grid(row = 1, column = 0, sticky = W )
        a = Label(self, text = '        Sorry you\'re trapped now, you have to exit to go back     ', bg = 'gold', font = ('Arial', 14,'bold'))
        a.grid(row = 2, column = 0, sticky = W)
        b = Button(self,command=self.goback,bg="black")
        b.grid(row=14,column=3,sticky=S)

    def goback(self):
        self.closefile()