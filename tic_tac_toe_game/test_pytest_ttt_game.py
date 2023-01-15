"""
@author:    Krzysztof Brzozowski
@file:      test_pytest_ttt_game
@time:      15/01/2023
@desc:      
"""
import pytest
from tic_tac_toe_game.ttt_game import *

# TODO how to put param into parametrize?


@pytest.mark.parametrize("play_field, expected_result", [
    ([[None, None, None], [None, None, None], [None, None, None]], None),
    ([['x', None, None], [None, None, None], [None, None, None]], None),
    ([[None, None, None], [None, None, None], ['x', None, None]], None),
    ([[None, None, 'x'], [None, None, None], [None, None, None]], None),
    ([[None, None, None], [None, None, None], [None, None, 'x']], None),
    ([['x', 'x', 'x'], [None, None, None], [None, None, None]], '--->  Player None won -> row equal'),
    ([[None, None, None], ['x', 'x', 'x'], [None, None, None]], '--->  Player None won -> row equal'),
    ([[None, None, None], [None, None, None], ['x', 'x', 'x']], '--->  Player None won -> row equal'),
    ([['x', None, None], ['x', None, None], ['x', None, None]], '--->  Player None won -> column equal'),
    ([[None, 'x', None], [None, 'x', None], [None, 'x', None]], '--->  Player None won -> column equal'),
    ([[None, None, 'x'], [None, None, 'x'], [None, None, 'x']], '--->  Player None won -> column equal'),
    ([['x', None, None], [None, 'x', None], [None, None, 'x']], '--->  Player None won -> diagonal equal'),
    ([[None, None, 'x'], [None, 'x', None], ['x', None, None]], '--->  Player None won -> -diagonal equal'),
])
class TestTicTacToeGame:
    @pytest.fixture(autouse=True)
    def setup_startup(self):
        self.tic_tac_toe_game = TTTGame()
        self.test_player = 0

    def test_empty_field(self, play_field, expected_result):
        self.tic_tac_toe_game.play_field = play_field
        assert self.tic_tac_toe_game.verify_win() == expected_result
