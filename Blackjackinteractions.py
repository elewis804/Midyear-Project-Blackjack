import random
class interactions(object):
    def __init__(self):
        self.hand = []
    def start_the_hand(self):
        card1 = random.randrange(1,14)
        card1 = str(card1)
        if card1 == "13":
            card1 = "King"
        elif card1 == "12":
            card1 = "Queen"
        elif card1 == "11":
            card1 = "Jack"
        self.hand.append(card1)
        card2 = random.randrange(1, 14)
        card2 = str(card2)
        if card2 == "13":
            card2 = "King"
        elif card2 == "12":
            card2= "Queen"
        elif card2 == "11":
            card2= "Jack"
        self.hand.append(card2)

    def addcard(self):
        card1 = random.randrange(1, 14)
        card1 = str(card1)
        if card1 == "13":
            card1 = "King"
        elif card1 == "12":
            card1 = "Queen"
        elif card1 == "11":
            card1 = "Jack"
        self.hand.append(card1)
    def compare(self):
