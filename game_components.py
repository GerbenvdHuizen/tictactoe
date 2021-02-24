from typing import Dict, Optional


class Player:

    def __init__(self, marking: str):
        self.marking = marking

    def __str__(self) -> str:
        return f'Player with marking {self.marking}'


class Board:

    def __init__(self):
        self.board = {
            '1': ' ', '2': ' ', '3':  ' ',
            '4': ' ', '5': ' ', '6':  ' ',
            '7': ' ', '8': ' ', '9':  ' '
        }

    def show_board_state(self):
        """Prints the current board state."""
        print(f"{self.board['1']}|{self.board['2']}|{self.board['3']}")
        print("-+-+-")
        print(f"{self.board['4']}|{self.board['5']}|{self.board['6']}")
        print("-+-+-")
        print(f"{self.board['7']}|{self.board['8']}|{self.board['9']}")

    def update_board_state(self, position: str, player: Player) -> Optional[Dict[str, str]]:
        def move_validity_check(board: Dict[str, str]) -> bool:
            if board[position] == ' ':
                return True
            return False

        # If move is valid return new board state, else return None.
        if move_validity_check(self.board):
            self.board[position] = player.marking
            return self.board
        return None

    def check_winning_state(self, player: Player) -> bool:
        winning_states = [
            # Horizontal wins states
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            # Vertical wins states
            ['1', '4', '7'],
            ['2', '5', '8'],
            ['3', '6', '9'],
            # Diagonal win states
            ['1', '5', '9'],
            ['7', '5', '3']
        ]
        for outer1, inner, outer2 in winning_states:
            if self.board[outer1] == self.board[inner] == self.board[outer2] == player.marking:
                return True
        return False

    def board_is_full(self) -> bool:
        return all(value != ' ' for cell, value in self.board.items())
