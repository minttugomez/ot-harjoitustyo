import random

class MemoryGame:
    def __init__(self, cards):
        self.cards = cards
        self.grid = [[],[],[],[],[],[],[],[]]

    def validate_cards(self):
        length = len(self.cards)
        if length == 36:
            pass
        elif length < 36:
            for i in range (36-length):
                self.cards.append(i+length+1)
        elif length > 36:
            self.cards = self.cards[:36]
        return self.cards

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def create_grid(self, rows, cols):
        self.grid = [self.cards[i:i+cols] for i in range(0, len(self.cards), cols)]

    def start(self):
        pass

    def end(self):
        pass