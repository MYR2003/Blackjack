from random import randrange as rand

class card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
    def __str__(self):
        return f'{self.number} of {self.suit}'
    def number(self):
        return self.number
    def suit(self):
        return self.suit
    
class deck:
    numbers = ["2","3","4","5",
              "6","7","8","9", 
              "10","Jack","Queen",
              "King","Ace"]
    suits = ["Hearts", "Clubs",
            "Diamonds", "Spades"]
    deck = []
    def __init__(self, numb=1):
        self.numb = numb
    def create_deck(self):
        for g in range(self.numb):
            for i in self.numbers:
                for e in self.suits:
                    a = card(i,e)
                    self.deck.append(a)
        return print("Deck created")
    def __str__(self):
        return f'This is a deck'
    def shuffle(self):
        new_deck = []
        N = len(self.deck)
        for i in range(N):
            n = len(self.deck)
            a = self.deck.pop(rand(0,n))
            new_deck.append(a)
        self.deck = new_deck
        return
    def take_card(self):
        a = self.deck.pop()
        return a
    def length_of_deck(self):
        N = len(self.deck)
        return N