"""
@author:    Krzysztof Brzozowski
@file:      ttt_game
@time:      15/01/2023
@desc:      
"""


class TTTGame:
    def __init__(self):
        self.play_field = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.current_point = 0

    def _print_play_field(self):
        [print(row) for row in self.play_field]

    def _set_play_field(self, x_coordinates: int, y_coordinates: int, value: str|int):
        self.play_field[x_coordinates][y_coordinates] = value
        self.current_point += 1

    def set_sign_user(self, user_id: str|int, user_sign: str|int):
        while True:
            x_coordinates, y_coordinates = map(int, input('Provide X and Y coordinates for your point').split(','))

            if self.play_field[x_coordinates][y_coordinates] is not None:
                print('This point is already set')
                continue

            print(f'User {user_id} set {x_coordinates=}, {y_coordinates=}')
            self._set_play_field(x_coordinates=x_coordinates, y_coordinates=y_coordinates, value=user_sign)
            self._print_play_field()
            break

    def verify_win(self):
        for idx in range(3):
            if len(set(i for i in self.play_field[idx])) == 1 \
                    and next(iter(set(i for i in self.play_field[idx]))):
                return 'row equal'

            if len(set(row[idx] for row in self.play_field)) == 1 \
                    and next(iter(set(row[idx] for row in self.play_field))) is not None:
                return 'column equal'

            if len({self.play_field[p][p] for p in range(3)}) == 1:
                return 'diagonal equal'

            if len({self.play_field[-p - 1][p] for p in range(3)}) == 1:
                return '-diagonal equal'


if __name__ == '__main__':
    tic_tac_toe_game = TTTGame()
    while True:
        tic_tac_toe_game.set_sign_user(0, 'x')
        tic_tac_toe_game.set_sign_user(1, 'o')
        tic_tac_toe_game.verify_win()
