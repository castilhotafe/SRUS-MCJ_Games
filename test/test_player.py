import unittest
import random
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

    def test_custom_sort_players(self):
        marcus = Player('01','Marcus')
        sarcus = Player('02', 'Sarcus', 20)
        rascum = Player('3', 'Rascum', 10)
        urksam = Player('07', 'Urksam', 15)

        players = [
            marcus,
            sarcus,
            rascum,
            urksam
        ]

        sorted_players = Player.sort_players(players)

        expected_players = [
            sarcus,
            urksam,
            rascum,
            marcus
        ]
        self.assertEqual(sorted_players,expected_players)
        self.assertNotEqual(players[0],expected_players[0])

    def test_sort_players_scaled(self):
        players = [Player(f'{i:03}',f'Player {i}', score=random.randint(0, 1000)) for i in range(1000)]

        builtin_sorted = sorted(players, reverse=True)

        custom_sort = Player.sort_players(players)
        self.assertEqual(builtin_sorted, custom_sort)

    def test_sort_players_list_already_sorted(self):
        players = [Player(f'{i:03}',f'Player {i}', score=random.randint(0, 1000)) for i in range(1000)]
        sorted_players = sorted(players,reverse=True)

        custom_sort = Player.sort_players(sorted_players)
        self.assertEqual(sorted_players,custom_sort)