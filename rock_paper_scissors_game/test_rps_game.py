"""
@author:    Krzysztof Brzozowski
@file:      tests_rsp_game
@time:      1/11/2023
@desc:  
"""
import unittest

from main import *


class RPSTests(unittest.TestCase):
    def setUp(self):
        self.rsp_game = Game()

    def test_init_input_raise_error(self):
        with self.assertRaises(NotImplementedError):
            self.rsp_game.input_decoder('X')

    def test_win_configs(self):
        expected_response = 'User win'

        self.rsp_game.user_choice = 'paper'
        self.rsp_game.computer_choice = 'rock'

        self.assertEqual(self.rsp_game.compare_result(), expected_response)

        self.rsp_game.user_choice = 'rock'
        self.rsp_game.computer_choice = 'scissors'

        self.assertEqual(self.rsp_game.compare_result(), expected_response)

        self.rsp_game.user_choice = 'scissors'
        self.rsp_game.computer_choice = 'paper'

        self.assertEqual(self.rsp_game.compare_result(), expected_response)

    def test_lose_configs(self):
        expected_response = 'Computer win'

        self.rsp_game.user_choice = 'paper'
        self.rsp_game.computer_choice = 'scissors'

        self.assertEqual(self.rsp_game.compare_result(), expected_response)

        self.rsp_game.user_choice = 'scissors'
        self.rsp_game.computer_choice = 'rock'

        self.assertEqual(self.rsp_game.compare_result(), expected_response)

        self.rsp_game.user_choice = 'rock'
        self.rsp_game.computer_choice = 'paper'

        self.assertEqual(self.rsp_game.compare_result(), expected_response)

    def test_draw_config(self):
        expected_response = 'Draw'

        self.rsp_game.user_choice = 'paper'
        self.rsp_game.computer_choice = 'paper'

        self.assertEqual(self.rsp_game.compare_result(), expected_response)

        self.rsp_game.user_choice = 'scissors'
        self.rsp_game.computer_choice = 'scissors'

        self.assertEqual(self.rsp_game.compare_result(), expected_response)

        self.rsp_game.user_choice = 'rock'
        self.rsp_game.computer_choice = 'rock'

        self.assertEqual(self.rsp_game.compare_result(), expected_response)
