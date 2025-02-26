import chess

class Chess:
    def __init__(self, board=None) -> None:
        self.board = board if board is not None else chess.Board()

    def move_piece(self, move: str) -> bool:
        if self.is_legal_move(move):
            self.board.push_san(move)
            return True
        return False

    def undo_move(self) -> bool:
        if self.board.move_stack:
            self.board.pop()
            return True
        return False

    def is_legal_move(self, move: str) -> bool:
        return move in self.get_legal_moves()

    def get_legal_moves(self) -> list:
        return [self.board.san(move) for move in self.board.legal_moves]

    def get_board_ascii(self) -> str:
        return str(self.board)

    def get_board_fen(self) -> str:
        return self.board.fen()

    def reset_board(self) -> None:
        self.board.reset()

    def game_over(self) -> bool:
        return (
            self.board.is_checkmate()
            or self.board.is_stalemate()
            or self.board.is_insufficient_material()
            or self.board.can_claim_fifty_moves()
            or self.board.can_claim_threefold_repetition()
        )

    def get_winner(self) -> str:
        if self.board.is_checkmate():
            return "Black" if self.board.turn else "White"
        elif self.board.is_stalemate() or self.board.is_insufficient_material() or self.board.can_claim_fifty_moves() or self.board.can_claim_threefold_repetition():
            return "Draw"
        return "In Progress"
