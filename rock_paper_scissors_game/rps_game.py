"""
@author:    Krzysztof Brzozowski
@file:      rps_game
@time:      1/11/2023
@desc:  
"""
import random


class RPSGame:
    def __init__(self):
        self.user_choice = None
        self.computer_choice = None
        self.win_configs = {
            'paper':    'rock',
            'rock':     'scissors',
            'scissors': 'paper'
        }

    def get_computer_choice(self):
        """Select random number from 1 to 3
        """
        match random.randint(1, 3):
            case 1: self.computer_choice = 'paper'
            case 2: self.computer_choice = 'rock'
            case 3: self.computer_choice = 'scissors'
            case _:
                raise NotImplementedError('Computer did not decide')

    def input_decoder(self, input_string: str = None):
        match input_string.lower():
            case 'p': self.user_choice = 'paper'
            case 'r': self.user_choice = 'rock'
            case 's': self.user_choice = 'scissors'
            case 'e': exit('Exiting program')
            case _:
                raise NotImplementedError('Select correct option (p)aper, (r)ock, (s)cissors, (e)xit')

    def compare_result(self):
        print(f'{self.user_choice=}, {self.computer_choice=}')
        if self.user_choice == self.computer_choice:
            return 'Draw'

        for key, value in self.win_configs.items():
            if key == self.user_choice and value == self.computer_choice:
                return 'User win'

        return 'Computer win'


if __name__ == '__main__':
    while True:
        user_choice = input('Select one choice: (p)aper, (r)ock, (s)cissors, (e)xit\n')
        rsp_game = RPSGame()

        rsp_game.input_decoder(user_choice)
        rsp_game.get_computer_choice()

        print(f'---> {rsp_game.compare_result()}')

