import random
import pygame

class MemoryGame:

    """ Class for handling game logic and game situation

    Attributes:
        cards: list of 36 items that will be turned into 72 cards """

    def __init__(self, cards):

        """ Constuctor for the class. Creates a playable game.

        Args:
            cards: list of 36 items """

        self.cards = cards
        self.grid = [[], [], [], [], [], [], [], []]
        self.players = 0
        self.points = {}
        self.started = False
        self.turn = 0
        self.opened_cards = []

        pygame.init()
        self.font = pygame.font.Font(None, 100)

    def validate_cards(self):

        """ Makes sure there is right amount of cards.
        If there's too many, the extra ones are removed. If there is too little, new ones are added.

        Returns:
            cards: validated cards """

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

        """ The 36 cards are turned into 72 cards, each of which has a pair. """

        cards_copy = self.cards.copy()
        self.cards.extend(cards_copy)

    def shuffle_cards(self):

        """ Shuffles the cards into a random order. """

        random.shuffle(self.cards)

    def create_grid(self, cols):

        """ Turns the list of cards into a grid (aka list of lists).

        Args:
            cols: in how many colums the cards will be divided into (default=9) """

        self.grid = [[self.font.render(str(card), True, (0, 0, 0)) for card in self.cards[i:i+cols]]
                    for i in range(0, len(self.cards), cols)]

    def setup(self):

        """ Sets things up. Runs through all the fundamental methods. """

        self.validate_cards()
        self.duplicate_cards()
        self.shuffle_cards()
        self.create_grid(9)

    def start(self):

        """ Updates the game status and gives the turn to the first player. """

        self.started = True
        self.next_turn()

    def end(self):

        """ Resets the players when the game is over. """

        self.players = 0

    def choose_card(self, row, col, player):

        """ Runs when a card is clicked.
        Checks if it's the first or second card opened.
        When the second card is opened, check_match() is run.
        If the cards are a match, a point will be given to player.

        Args:
            row: which row the clicked card is in
            col: which column the clicked card is in
            player: whose turn it is

        Returns:
            True if the two cards were opened, False if only one card was opened  """

        if len(self.opened_cards) == 0:
            self.opened_cards.append((row, col, self.grid[row-1][col-1]))
        else:
            if row != self.opened_cards[0][0] or col != self.opened_cards[0][1]:
                self.opened_cards.append((row, col, self.grid[row-1][col-1]))

        if len(self.opened_cards) == 2:
            match = self.check_match()
            if match:
                self.add_points(player)
            return True
        return False

    def check_match(self):

        """ Checks if the cards are a match.
            -- logic not created yet-- """

        return False # add logic here later

    def change_players(self, players):

        """ Changes the amount of players in the game.
        Makes sure the amount of players is 2-4. Sets everyone's points to 0.

        Args:
            players: number of players """

        if 1 < players < 5:
            self.players = players
            self.points = {i+1: 0 for i in range(players)}

    def get_points(self):

        """ Returns player points

        Returns:
            points: everyone's points  """

        return self.points

    def add_points(self, player):

        """ Adds a point to set player.

        Args:
            player: which player the point is added to """

        if player in self.points:
            self.points[player] += 1

    def is_started(self):

        """ Returns the game status.

        Returns:
            started: True if game is started, False if it's not  """

        return self.started

    def next_turn(self):

        """ Switches the turn to the next player. """

        self.opened_cards = []
        if self.turn < self.players:
            self.turn += 1
        else:
            self.turn = 1

    def get_turn(self):

        """ Returns whose turn it is.

        Returns:
            turn: whose turn it is  """

        return self.turn

    def get_picture(self, row, col):

        """ Returns the picture in a specific place.

        Args:
            row: which row the picture is on
            col: which column the picture is on
        Returns:
            picture as a surface  """

        return self.grid[row-1][col-1]

    def get_opened_cards(self):

        """ Returns how many cards are open.

        Returns:
            opened cards: the amount of cards open """

        return len(self.opened_cards)
