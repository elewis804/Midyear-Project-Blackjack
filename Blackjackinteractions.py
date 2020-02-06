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
        if x.name == "Ace":
            if self.score + 11 > 21:
                x.value = 1
            elif self.score + 11 <= 21:
                x.value = 11
        self.hand.append(x)
        for z in range(len(self.hand)):
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
    def comparecard(self,player2):
        if self.score > player2.score:
            self.win += 1
            return "Player 1 has won"
        elif self.score == player2.score:
            return "It is a tie!"
        else:
            player2.win += 1
            return "Player 2 has won!"