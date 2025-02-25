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

    def game_over(self) -> bool:
        if self.board.is_checkmate():
            return True
        elif self.board.is_stalemate():
            return True
        elif self.board.is_insufficient_material():
            return True
        elif self.board.can_claim_fifty_moves():
            return True
        elif self.board.can_claim_threefold_repetition():
            return True
        else:
            return False
