"""
@author:    Krzysztof Brzozowski
@file:      test_ttt_game
@time:      15/01/2023
@desc:      
"""
import unittest

from tic_tac_toe_game.ttt_game import *


class TTTTests(unittest.TestCase):
    def setUp(self):
        self.tic_tac_toe_game = TTTGame()
        self.tic_tac_toe_game.current_player = 0
        self.test_player = 0

    def test_empty_field(self):
        self.tic_tac_toe_game.play_field = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), None)

    def test_one_sign_corner_0_0(self):
        self.tic_tac_toe_game.play_field = [
            ['x', None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), None)

    def test_one_sign_corner_0_2(self):
        self.tic_tac_toe_game.play_field = [
            [None, None, None],
            [None, None, None],
            ['x', None, None]
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), None)

    def test_one_sign_corner_2_0(self):
        self.tic_tac_toe_game.play_field = [
            [None, None, 'x'],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), None)

    def test_one_sign_corner_2_2(self):
        self.tic_tac_toe_game.play_field = [
            [None, None, None],
            [None, None, None],
            [None, None, 'x']
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), None)

    def test_row_result(self):
        self.tic_tac_toe_game.play_field = [
            ['x', 'x', 'x'],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), f'player {self.test_player} won -> row equal')

    def test_negative_row_result(self):
        self.tic_tac_toe_game.play_field = [
            ['x', 'o', 'x'],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), None)

    def test_column_result(self):
        self.tic_tac_toe_game.play_field = [
            ['x', None, None],
            ['x', None, None],
            ['x', None, None]
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), f'player {self.test_player} won -> column equal')

    def test_negative_column_result(self):
        self.tic_tac_toe_game.play_field = [
            ['x', None, None],
            ['o', None, None],
            ['x', None, None]
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), None)

    def test_diagonal_result(self):
        self.tic_tac_toe_game.play_field = [
            ['x', None, None],
            [None, 'x', None],
            [None, None, 'x']
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), f'player {self.test_player} won -> diagonal equal')

    def test_negative_diagonal_result(self):
        self.tic_tac_toe_game.play_field = [
            ['x', None, None],
            [None, 'o', None],
            [None, None, 'x']
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), None)

    def test_diagonal_reverse_result(self):
        self.tic_tac_toe_game.play_field = [
            [None, None, 'x'],
            [None, 'x', None],
            ['x', None, None]
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), f'player {self.test_player} won -> -diagonal equal')

    def test_negative_diagonal_reverse_result(self):
        self.tic_tac_toe_game.play_field = [
            [None, None, 'x'],
            [None, 'o', None],
            ['x', None, None]
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), None)


