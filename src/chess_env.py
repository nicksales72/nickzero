import chess

class Chess:
    def __init__(self, board=None) -> None:
        self.board = board if board is not None else chess.Board()

    def move_piece(self, move: str) -> None:
        self.board.push_san(move)

    def is_legal_move(self, move: str) -> bool:
        try:
            parsed_move = self.board.parse_san(move)
            return parsed_move in self.board.legal_moves
        except ValueError:
            return False
