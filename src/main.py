from chess_env import Chess

def game_loop(game) -> None:
    while not game.game_over():
        print(game.get_board_ascii())
        turn = "White" if game.board.turn else "Black" # White == T, Black == F
        move = input(f"{turn} to move: ")

        if not game.move_piece(move): print("Invalid move.")
    
    game.reset_board()
    print(game.get_board_ascii())
    print(f"{game.get_winner()} wins.")


if __name__ == "__main__":
    game = Chess()
    game_loop(game)
