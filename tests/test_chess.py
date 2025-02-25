import unittest 
from src.chess_env import Chess

class TestChess(unittest.TestCase):
    def setUp(self):
        self.game = Chess()

    def test_init_board(self):
        self.assertTrue(self.game.board.is_valid())
        print(self.game.board)

    def test_legal_move(self):
        self.game.move_piece("e4")
        self.assertEqual(self.game.board.fullmove_number, 1)
        self.assertEqual(self.game.board.turn, False)
        print(self.game.board)

if __name__ == "__main__":
    unittest.main()
