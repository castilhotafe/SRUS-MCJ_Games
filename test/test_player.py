import unittest
from app.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player_zero = Player("00", "Marcos")

    def test_player_properties(self):
        self.assertEqual(self.player_zero.uid, "00")
        self.assertEqual(self.player_zero.name, "Marcos")

    def test_sort_players(self):
        players = [Player('01', "Alice", score=10), Player('02','Bob', score=5),
                   Player('03','Charlie', score=15)]
        # note: ensure initialization code is valid for **your** implementation.
        # For example, is your parameter called uid? is the first parameter name?

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player('02','Bob', score=5), Player('01','Alice', score=10),
                                   Player('03','Charlie', score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player('01','Alice', score=10)
        bob = Player('02','Bob', score=5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(alice != bob, "score not equals")
        # or, event better
        self.assertLess(bob, alice)