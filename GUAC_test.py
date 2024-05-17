import unittest
from GUAC import GUAC

class TestGUAC(unittest.TestCase):
    def setUp(self):
        self.guac = GUAC()

    def test_init(self):
        self.assertIsNone(self.guac.sequence)
        self.assertIsNone(self.guac.mRNA_sequence)
        self.assertEqual(self.guac.scoreboard, {})
        self.assertEqual(self.guac.players, {})
        self.assertFalse(self.guac.game_over)

    def test_add_player(self):
        self.guac.add_player('player1', '192.168.1.1')
        self.assertIn('player1', self.guac.players)
        self.assertIn('player1', self.guac.scoreboard)

    def test_generate_sequence(self):
        self.guac.generate_sequence()
        self.assertIsNotNone(self.guac.sequence)

    def test_checker(self):
        self.guac.sequence = 'ATGC'
        self.assertTrue(self.guac.checker('player1', 'ATGC', 1234567890))
        self.assertFalse(self.guac.checker('player1', 'TGCA', 1234567890))

    def test_scoreboard(self):
        self.guac.add_player('player1', '192.168.1.1')
        self.guac.add_player('player2', '192.168.1.2')
        scoreboard = self.guac.scoreboard()
        self.assertIn('player1', scoreboard)
        self.assertIn('player2', scoreboard)

if __name__ == '__main__':
    unittest.main()