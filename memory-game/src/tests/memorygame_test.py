import unittest
import pygame
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
        self.assertEqual(self.memorygame.turn, 0)
        self.assertEqual(self.memorygame.started, False)
        self.assertEqual(self.memorygame.ended, False)

    def test_validation_when_right_amount_of_cards(self):
        self.memorygame.validate_cards()
        self.assertEqual(self.memorygame.cards, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9),
                                (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18),
                                (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27),
                                (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)])

    def test_validation_when_too_little_cards(self):
        cards = list(range(1, 19))
        self.memorygame = MemoryGame(cards)
        self.memorygame.validate_cards()
        self.assertEqual(self.memorygame.cards, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9),
                                (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18),
                                (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27),
                                (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)])

    def test_validation_when_too_many_cards(self):
        cards = list(range(1, 46))
        self.memorygame = MemoryGame(cards)
        self.memorygame.validate_cards()
        self.assertEqual(self.memorygame.cards, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9),
                                (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18),
                                (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27),
                                (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)])

    def test_shuffle(self):
        self.memorygame.shuffle_cards()
        self.assertEqual(len(self.memorygame.cards), len(self.cards))
        self.assertNotEqual(self.memorygame.cards, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9),
                                (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18),
                                (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27),
                                (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)])

    def test_grid_creation(self):
        self.memorygame.validate_cards()
        self.memorygame.duplicate_cards()
        self.memorygame.create_grid(9)
        all_surface = all(isinstance(item[0], pygame.Surface) for row in self.memorygame.grid for item in row)
        self.assertTrue(all_surface)
        
    def test_setup(self):
        self.memorygame.setup()
        self.assertEqual(len(self.memorygame.grid), 8)
    
    def test_start(self):
        self.memorygame.start()
        is_started = self.memorygame.is_started()
        self.assertEqual(is_started, True)

    def test_end(self):
        self.memorygame.change_players(2)
        self.memorygame.end()
        self.assertEqual(self.memorygame.is_started(), False)
        self.assertEqual(self.memorygame.is_ended(), True)

    def test_back_to_menu(self):
        self.memorygame.change_players(2)
        self.memorygame.end()
        self.memorygame.back_to_menu()
        self.assertEqual(self.memorygame.is_started(), False)
        self.assertEqual(self.memorygame.is_ended(), False)
        self.assertEqual(self.memorygame.players, 0)
        self.assertEqual(self.memorygame.get_points(), {})

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
        
    def test_too_many_players(self):
        self.memorygame.change_players(5)
        self.assertEqual(self.memorygame.players, 0)

    def test_negative_players(self):
        self.memorygame.change_players(-1)
        self.assertEqual(self.memorygame.players, 0)

    def test_get_points(self):
        self.memorygame.change_players(2)
        self.assertEqual(self.memorygame.get_points(), {1:0, 2:0})

    def test_add_points(self):
        self.memorygame.change_players(2)
        self.memorygame.add_points(2)
        self.assertEqual(self.memorygame.get_points(), {1:0, 2:1})

    def test_add_points_to_nonexistent_player(self):
        self.memorygame.change_players(2)
        self.memorygame.add_points(3)
        self.assertEqual(self.memorygame.get_points(), {1:0, 2:0})

    def test_is_started(self):
        is_started = self.memorygame.is_started()
        self.assertEqual(is_started, False)

    def test_choose_card_first_card(self):
        self.memorygame.grid = [[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)],
                                [(10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)],
                                [(19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27)],
                                [(28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)],
                                [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)],
                                [(10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)],
                                [(19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27)],
                                [(28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)]]
        boolean = self.memorygame.choose_card(0, 0, 1)
        self.assertEqual(self.memorygame.opened_cards, [(0, 0, (1, 1))])
        self.assertEqual(boolean, False)
    
    def test_choose_card_second_card(self):
        self.memorygame.grid = [[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)],
                                [(10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)],
                                [(19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27)],
                                [(28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)],
                                [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)],
                                [(10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)],
                                [(19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27)],
                                [(28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)]]
        self.memorygame.choose_card(0, 0, 1)
        boolean = self.memorygame.choose_card(0, 1, 1)
        self.assertEqual(self.memorygame.opened_cards, [(0, 0, (1, 1)), (0, 1, (2, 2))])
        self.assertEqual(boolean, True)

    def test_next_turn(self):
        self.memorygame.next_turn()
        turn = self.memorygame.get_turn()
        self.assertEqual(turn, 1)
    
    def test_next_turn_part_2(self):
        self.memorygame.change_players(2)
        self.memorygame.next_turn()
        self.memorygame.next_turn()
        turn = self.memorygame.get_turn()
        self.assertEqual(turn, 2)

    def test_new_turn(self):
        self.memorygame.change_players(2)
        self.memorygame.next_turn()
        self.memorygame.new_turn()
        turn = self.memorygame.get_turn()
        self.assertEqual(turn, 1)

    def test_get_picture(self):
        self.memorygame.grid = [[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)],
                                [(10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)],
                                [(19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27)],
                                [(28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)],
                                [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)],
                                [(10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)],
                                [(19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27)],
                                [(28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)]]
        picture = self.memorygame.get_picture(1, 3)
        self.assertEqual(picture, 13)

    def test_get_open_cards(self):
        self.memorygame.grid = [[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)],
                                [(10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)],
                                [(19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27)],
                                [(28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)],
                                [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)],
                                [(10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)],
                                [(19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27)],
                                [(28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)]]
        self.memorygame.choose_card(1, 1, 1)
        self.assertEqual(self.memorygame.get_opened_cards(), 1)

    def test_open_same_card(self):
        self.memorygame.grid = [[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)],
                                [(10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)],
                                [(19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27)],
                                [(28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)],
                                [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)],
                                [(10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)],
                                [(19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27)],
                                [(28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)]] 
        self.memorygame.choose_card(0, 0, 1)
        self.memorygame.choose_card(0, 0, 1)
        self.assertEqual(self.memorygame.opened_cards, [(0, 0, (1, 1))])   

    def test_match(self):
        self.memorygame.change_players(2)
        self.memorygame.grid = [[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)],
                                [(10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)],
                                [(19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27)],
                                [(28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)],
                                [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)],
                                [(10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)],
                                [(19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27)],
                                [(28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36)]] 
        self.memorygame.choose_card(0, 0, 1)
        self.memorygame.choose_card(4, 0, 1)
        self.assertEqual(self.memorygame.get_points(), {1:1, 2:0})
        self.assertEqual(self.memorygame.get_match(), [(0, 0, (1, 1)), (4, 0, (1, 1))])
