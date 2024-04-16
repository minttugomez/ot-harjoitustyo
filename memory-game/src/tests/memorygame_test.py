import unittest
from memorygame import MemoryGame

class TestMemorygame(unittest.TestCase):
    def setUp(self):
        self.cards = list(range(1, 37))
        self.memorygame = MemoryGame(self.cards)

    def test_initialization(self):
        self.assertEqual(self.memorygame.cards, list(range(1, 37)))
        self.assertEqual(self.memorygame.grid, [
                         [], [], [], [], [], [], [], []])
        self.assertEqual(self.memorygame.players, 0)

    def test_validation_when_right_amount_of_cards(self):
        self.memorygame.validate_cards()
        self.assertEqual(self.memorygame.cards, list(range(1, 37)))

    def test_validation_when_too_little_cards(self):
        cards = list(range(1, 19))
        self.memorygame = MemoryGame(cards)
        self.memorygame.validate_cards()
        self.assertEqual(self.memorygame.cards, list(range(1, 37)))

    def test_validation_when_too_many_cards(self):
        cards = list(range(1, 46))
        self.memorygame = MemoryGame(cards)
        self.memorygame.validate_cards()
        self.assertEqual(self.memorygame.cards, list(range(1, 37)))

    def test_shuffle(self):
        self.memorygame.shuffle_cards()
        self.assertEqual(len(self.memorygame.cards), len(self.cards))
        self.assertNotEqual(self.memorygame.cards, list(range(1, 37)))

    def test_grid_creation(self):
        self.memorygame.create_grid(9)
        self.assertEqual(self.memorygame.grid, [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                [10, 11, 12, 13, 14, 15, 16, 17, 18],
                                                [19, 20, 21, 22, 23, 24, 25, 26, 27],
                                                [28, 29, 30, 31, 32, 33, 34, 35, 36]])
        
    def test_start(self):
        self.memorygame.start()
        self.assertEqual(len(self.memorygame.grid), 8)
        self.assertNotEqual(self.memorygame.grid, [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                [10, 11, 12, 13, 14, 15, 16, 17, 18],
                                                [19, 20, 21, 22, 23, 24, 25, 26, 27],
                                                [28, 29, 30, 31, 32, 33, 34, 35, 36],
                                                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                [10, 11, 12, 13, 14, 15, 16, 17, 18],
                                                [19, 20, 21, 22, 23, 24, 25, 26, 27],
                                                [28, 29, 30, 31, 32, 33, 34, 35, 36]])

    def test_end(self):
        self.memorygame.end()

    def test_change_players(self):
        self.memorygame.change_players(4)
        self.assertEqual(self.memorygame.players, 4)

    def test_duplicate_cards(self):
        self.memorygame.duplicate_cards()
        self.assertEqual(self.memorygame.cards, [1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                10, 11, 12, 13, 14, 15, 16, 17, 18,
                                                19, 20, 21, 22, 23, 24, 25, 26, 27,
                                                28, 29, 30, 31, 32, 33, 34, 35, 36,
                                                1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                10, 11, 12, 13, 14, 15, 16, 17, 18,
                                                19, 20, 21, 22, 23, 24, 25, 26, 27,
                                                28, 29, 30, 31, 32, 33, 34, 35, 36])
