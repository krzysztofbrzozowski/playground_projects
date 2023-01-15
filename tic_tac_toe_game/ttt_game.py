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
        self.current_player = None

    def _print_play_field(self):
        [print(row) for row in self.play_field]

    def _set_play_field(self, x_coordinates: int, y_coordinates: int, value: str|int):
        self.play_field[x_coordinates][y_coordinates] = value
        self.current_point += 1

    def set_sign_user(self, user_id: str|int, user_sign: str|int):
        while True:
            y_coordinates, x_coordinates = map(int, input('Provide X and Y coordinates for your point\n').split(','))

            if self.play_field[x_coordinates][y_coordinates] is not None:
                print('This point is already set')
                continue

            print(f'User {user_id} set {x_coordinates=}, {y_coordinates=}')
            self.current_player = f'User {user_id}'
            self._set_play_field(x_coordinates=x_coordinates, y_coordinates=y_coordinates, value=user_sign)
            self._print_play_field()
            break

    def verify_win(self):
        for idx in range(3):
            if len(set(i for i in self.play_field[idx])) == 1 and \
                    next(iter(set(i for i in self.play_field[idx]))):
                return f'player {self.current_player} won -> row equal'

            if len(set(row[idx] for row in self.play_field)) == 1 and \
                    next(iter(set(row[idx] for row in self.play_field))) is not None:
                return f'player {self.current_player} won -> column equal'

        if len(set(self.play_field[p][p] for p in range(3))) == 1 and \
                next(iter(set(self.play_field[p][p] for p in range(3)))) is not None:
            return f'player {self.current_player} won -> diagonal equal'

        if len(set(self.play_field[-p - 1][p] for p in range(3))) == 1 and \
                next(iter(set(self.play_field[-p - 1][p] for p in range(3)))) is not None:
            return f'--->  Player {self.current_player} won -> -diagonal equal'

        return None


if __name__ == '__main__':
    tic_tac_toe_game = TTTGame()

    while True:
        for user_idx, user_sign in enumerate(['x', 'o']):
            tic_tac_toe_game.set_sign_user(user_idx, user_sign)
            if tic_tac_toe_game.verify_win() is not None:
                print(tic_tac_toe_game.verify_win())
                exit(0)
