import unittest
import game_logic.player as player1

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = player1.Player((255, 255, 255), 20, 1920, 1080)

    def test_player_constructor(self):
        return self.assertTupleEqual((self.player.n, self.player.width, self.player.height),(20, 1920, 1080))
        