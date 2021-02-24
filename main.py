from game import Game


def run_tictactoe():
    game = Game()
    game.show_board_info()
    player_turn = game.turn
    no_win_state = True
    while no_win_state:
        game.print_board_state()
        position = input(f'{player_turn}, show your move:')
        game.modify_board_state(position, player_turn)
        if game.check_if_player_has_win_state(player_turn):
            print(f'{player_turn} WINS!!!')
            game.print_board_state()
            break
        if game.check_if_player_has_tie_state(player_turn):
            print("It's a TIE!... GAME OVER!")
            game.print_board_state()
            break

        game.switch_player_turn()
        player_turn = game.turn


if __name__ == '__main__':
    run_tictactoe()
