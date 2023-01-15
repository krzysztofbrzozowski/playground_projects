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
    ([['x', 'x', 'x'], [None, None, None], [None, None, None]], 'player None won -> row equal'),
    ([[None, None, None], ['x', 'x', 'x'], [None, None, None]], 'player None won -> row equal'),
    ([[None, None, None], [None, None, None], ['x', 'x', 'x']], 'player None won -> row equal'),
    ([['x', None, None], ['x', None, None], ['x', None, None]], 'player None won -> column equal'),
    ([[None, 'x', None], [None, 'x', None], [None, 'x', None]], 'player None won -> column equal'),
    ([[None, None, 'x'], [None, None, 'x'], [None, None, 'x']], 'player None won -> column equal'),
    ([['x', None, None], [None, 'x', None], [None, None, 'x']], 'player None won -> diagonal equal'),
    ([[None, None, 'x'], [None, 'x', None], ['x', None, None]], 'player None won -> -diagonal equal'),
])
class TestTicTacToeGame:
    @pytest.fixture(autouse=True)
    def setup_startup(self):
        self.tic_tac_toe_game = TTTGame()
        self.test_player = 0

    def test_empty_field(self, play_field, expected_result):
        self.tic_tac_toe_game.play_field = play_field
        assert self.tic_tac_toe_game.verify_win() == expected_result
