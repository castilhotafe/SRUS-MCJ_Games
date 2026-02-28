import unittest
from player_list import PlayerList
from player import Player


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.my_player_00 = Player('1', 'Marcos')
        self.my_player_01 = Player('2', 'Socram')
        self.my_list = PlayerList()


    def test_is_empty(self):
        self.assertEqual(self.my_list.is_empty, True)


    def test_append_empty_list(self):
        self.my_list.append(self.my_player_00)
        self.assertFalse(self.my_list.is_empty)


    def test_append_not_empty_list(self):
        self.my_list.append(self.my_player_00)
        self.my_list.append(self.my_player_01)
        self.assertIsNotNone(self.my_list._head.next_player)
        self.assertIsNone(self.my_list._tail.next_player)


    def test_prepend_head_previous_is_none(self):
        self.my_list.prepend(self.my_player_00)
        self.my_list.prepend(self.my_player_01)
        self.assertEqual(self.my_list._head.next_player.player, self.my_player_00)
        self.assertIsNone(self.my_list._head._previous)
