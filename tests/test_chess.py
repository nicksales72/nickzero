import unittest
from src.chess_env import Chess

class TestChess(unittest.TestCase):
    def setUp(self):
        self.game = Chess()

    def test_init_board(self):
        self.assertTrue(self.game.board.is_valid())

        self.game.reset_board()

    def test_move(self):
        self.game.move_piece("e4")
        self.assertEqual(self.game.board.fullmove_number, 1)
        self.assertFalse(self.game.board.turn)

        self.game.reset_board()

    def test_legal_move(self):
        self.assertTrue(self.game.is_legal_move("e4"))
        self.assertTrue(self.game.is_legal_move("d4"))
        self.assertTrue(self.game.is_legal_move("Nf3"))
        self.assertTrue(self.game.is_legal_move("Nc3"))

        self.assertFalse(self.game.is_legal_move("e5"))
        self.assertFalse(self.game.is_legal_move("Kd1"))
        self.assertFalse(self.game.is_legal_move("h9"))
        self.assertFalse(self.game.is_legal_move("Qh5"))

        self.game.reset_board()

    def test_game_over(self):
        self.assertFalse(self.game.game_over())

        # Scholars mate
        self.game.move_piece("e4")
        self.game.move_piece("e5")
        self.game.move_piece("Qh5")
        self.game.move_piece("Nc6")
        self.game.move_piece("Bc4")
        self.game.move_piece("Nf6")
        self.game.move_piece("Qxf7#")
        self.assertTrue(self.game.game_over()) 

        self.game.reset_board()

if __name__ == "__main__":
    unittest.main()
