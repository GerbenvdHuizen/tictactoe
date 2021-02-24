from typing import Dict
from game_components import Board, Player


class Game:
    """Keeps track of players and current board state."""
    def __init__(self):
        self.playerX = Player('X')
        self.playerO = Player('O')
        self.board = Board()
        # Player X starts
        self.turn = self.playerX

    @staticmethod
    def show_board_info():
        print('These are the board valid board inputs you can use:')
        print("""
            1 - top left    | 2 - top middle    | 3 - top right
            4 - middle left | 5 - center        | 6 - middle right
            7 - bottom left | 8 - bottom middle | 9 - bottom right""")

    def print_board_state(self):
        self.board.show_board_state()

    def switch_player_turn(self):
        if self.turn is self.playerX:
            self.turn = self.playerO
        else:
            self.turn = self.playerX

    def check_if_player_has_win_state(self, player: Player) -> bool:
        return self.board.check_winning_state(player)

    def check_if_player_has_tie_state(self, player: Player) -> bool:
        return self.board.board_is_full() and not self.board.check_winning_state(player)

    def modify_board_state(self, position: str, player: Player) -> Dict[str, str]:
        while (new_board := self.board.update_board_state(position, player)) is None:
            position = input("The position you chose is unavailable. Please try again: ")
        return new_board
