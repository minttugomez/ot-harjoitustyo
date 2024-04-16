import random

class MemoryGame:
    def __init__(self, cards):
        self.cards = cards
        self.grid = [[], [], [], [], [], [], [], []]
        self.players = 0

    def validate_cards(self):
        length = len(self.cards)
        if length == 36:
            pass
        elif length < 36:
            for i in range(36-length):
                self.cards.append(i+length+1)
        else:
            self.cards = self.cards[:36]
        return self.cards

    def duplicate_cards(self):
        cards_copy = self.cards.copy()
        self.cards.extend(cards_copy)

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def create_grid(self, cols):
        self.grid = [self.cards[i:i+cols]
                     for i in range(0, len(self.cards), cols)]

    def start(self):
        self.validate_cards()
        self.duplicate_cards()
        self.shuffle_cards()
        self.create_grid(9)

    def end(self):
        pass

    def change_players(self, players):
        self.players = players
