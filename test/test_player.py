import unittest
from app.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player_zero = Player("00", "Marcos")


    def test_player_properties(self):
        self.assertEqual(self.player_zero.uid, "00")
        self.assertEqual(self.player_zero.name, "Marcos")




