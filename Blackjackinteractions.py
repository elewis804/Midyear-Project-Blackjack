import random

'''implement system to detect bust in screen_game'''


class card(object):
    def __init__(self,name,num,pic):
        self.name = name
        self.image = pic
        self.value = num





class Player(object):
    def __init__(self,file="Cards.txt"):
        self.score = 0
        self.hand = []
        self.lis1 = []
        self.lis2 = []
        self.lis3 = []
        self.lis4 = []
        self.textfile = open(file, "r")
        for x in self.textfile:
            x = x.strip()
            x = x.split(",")
            self.lis1.append(card(x[0],x[1],x[2]))
            self.lis2.append(card(x[0],x[1],x[2]))
            self.lis3.append(card(x[0],x[1],x[2]))
            self.lis4.append(card(x[0],x[1],x[2]))


    def getRandomCard(self):
        avail = len(self.lis1) + len(self.lis2) + len(self.lis3) + len(self.lis4) - 4
        lis = random.randint(0,avail)
        if lis <= len(self.lis1) - 1:
            lis = self.lis1
        elif lis <= len(self.lis1) - 1 + len(self.lis2) - 1:
            lis = self.lis2
        elif lis <= len(self.lis1) - 1 + len(self.lis2) - 1 + len(self.lis3) - 1:
            lis = self.lis3
        else:
            lis = self.lis4
        x = random.choice(lis)

        self.hand.append(x)
        self.score += x.value
        lis.remove(x)

