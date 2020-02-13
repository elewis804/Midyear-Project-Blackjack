import random

class card(object):
    def __init__(self,name,num,pic):
        self.name = name
        self.image = pic
        self.value = int(num)

class Player(object):
    def __init__(self,file="Cards.txt"):
        self.score = 0
        self.win = 0
        self.bust = False
        self.hand = []
        self.p_hand = []
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

    def getRandomCard(self,startup=False):
        '''
        print("Score at beginning of get_random: ",self.score)
        if len(self.hand) > 1:
            print("Hand at beginning of get_random: ",end="  ")
            for h in self.hand:
                print(h.name)
        '''
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
        if startup:
            if x.name == "Ace":
                if len(self.hand) < 1:
                    if x.name == "Ace":
                        x.value = 11
                else:
                    for g in self.hand:
                        if g.name == "Ace":
                            x.value = 1
        if not startup:
            if x.name == "Ace":
                if self.score + 11 > 21:
                    x.value = 1
                else:
                    x.value = 11
        self.hand.append(x)
        self.score += x.value
        if not startup:
            if x.name != "Ace":
                for z in range(len(self.hand)):
                    if z != len(self.hand)-1:
                        if self.hand[z].name == "Ace":
                            if self.score + 11 > 21:
                                self.hand[z].value = 1
                            else:
                                self.hand[z].value = 11
        self.score = 0
        for i in self.hand:
            self.score += i.value
        lis.remove(x)
        if self.score > 21:
            self.bust = True

    def clear_hand(self):
        for x in self.hand:
            self.hand.remove(x)
        if len(self.hand) != 0:
            del self.hand[0]