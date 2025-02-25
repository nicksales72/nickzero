import chess

class Chess:
    def __init__(self, board=None) -> None:
        self.board = board if board is not None else chess.Board()

    def move_piece(self, move: str) -> None:
        self.board.push_san(move)
