

"""
Unit tests for validating the functionality of the PlayerHashMap class.

This module provides a series of test cases to verify the behavior of
PlayerHashMap methods.
"""

import unittest


from app.player import Player
from app.player_hash_map import PlayerHashMap


class TestPlayerHashMap(unittest.TestCase):
    def setUp(self):
        """
        Sets up the necessary Player and PlayerHashMap objects for testing.

        This method initializes sample players and an empty hash map so each
        test starts from a clean and predictable state.
        """
        self.my_player_00 = Player('1', 'Marcos')
        self.my_player_01 = Player('2', 'Socram')
        self.my_player_02 = Player('3', 'Cosmar')
        self.my_hash_map = PlayerHashMap()

    def test_get_index_with_string_key(self):
        expected_index = Player.hash('1') % 10
        self.assertEqual(self.my_hash_map.get_index('1'), expected_index)

    def test_get_index_with_player_object(self):
        expected_index = hash(self.my_player_00) % 10
        self.assertEqual(self.my_hash_map.get_index(self.my_player_00), expected_index)

    def test_setitem_add_new_player(self):
        self.my_hash_map['1'] = 'Marcos'
        self.assertEqual(len(self.my_hash_map), 1)
        self.assertEqual(self.my_hash_map['1'].uid, '1')
        self.assertEqual(self.my_hash_map['1'].name, 'Marcos')

    def test_setitem_update_existing_player_name(self):
        self.my_hash_map['1'] = 'Marcos'
        self.my_hash_map['1'] = 'Updated Marcos'
        self.assertEqual(len(self.my_hash_map), 1)
        self.assertEqual(self.my_hash_map['1'].name, 'Updated Marcos')



    def test_delitem_removes_player(self):
        self.my_hash_map['1'] = 'Marcos'
        self.my_hash_map['2'] = 'Socram'
        del self.my_hash_map['1']
        self.assertEqual(len(self.my_hash_map), 1)


    def test_len_hash_map_with_multiple_players(self):
        self.my_hash_map['1'] = 'Marcos'
        self.my_hash_map['2'] = 'Socram'
        self.my_hash_map['3'] = 'Cosmar'
        self.assertEqual(len(self.my_hash_map), 3)