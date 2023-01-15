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

    def test_row_result(self):
        self.tic_tac_toe_game.play_field = [
            ['x', 'x', 'x'],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), 'row equal')

    def test_negative_row_result(self):
        self.tic_tac_toe_game.play_field = [
            ['x', 'o', 'x'],
            [None, None, None],
            [None, None, None]
        ]
        self.assertNotEqual(self.tic_tac_toe_game.verify_win(), 'row equal')

    def test_column_result(self):
        self.tic_tac_toe_game.play_field = [
            ['x', None, None],
            ['x', None, None],
            ['x', None, None]
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), 'column equal')

    def test_negative_column_result(self):
        self.tic_tac_toe_game.play_field = [
            ['x', None, None],
            ['o', None, None],
            ['x', None, None]
        ]
        self.assertNotEqual(self.tic_tac_toe_game.verify_win(), 'column equal')

    def test_diagonal_result(self):
        self.tic_tac_toe_game.play_field = [
            ['x', None, None],
            [None, 'x', None],
            [None, None, 'x']
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), 'diagonal equal')

    def test_negative_diagonal_result(self):
        self.tic_tac_toe_game.play_field = [
            ['x', None, None],
            [None, 'o', None],
            [None, None, 'x']
        ]
        self.assertNotEqual(self.tic_tac_toe_game.verify_win(), 'diagonal equal')

    def test_diagonal_reverse_result(self):
        self.tic_tac_toe_game.play_field = [
            [None, None, 'x'],
            [None, 'x', None],
            ['x', None, None]
        ]
        self.assertEqual(self.tic_tac_toe_game.verify_win(), '-diagonal equal')

    def test_negative_diagonal_reverse_result(self):
        self.tic_tac_toe_game.play_field = [
            [None, None, 'x'],
            [None, 'o', None],
            ['x', None, None]
        ]
        self.assertNotEqual(self.tic_tac_toe_game.verify_win(), '-diagonal equal')
