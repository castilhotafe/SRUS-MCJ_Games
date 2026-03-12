"""
Unit tests for validating the functionality of the PlayerList class.

This module provides a series of test cases to verify the behavior of
PlayerList methods. The tests include checks for appending, prepending,
and deleting players from the list in different scenarios. The setup
initializes instances of `Player` and `PlayerList` for reuse during
the test cases.

Classes
-------
TestPlayerList : unittest.TestCase
    Contains unit tests for the PlayerList class.
"""
import unittest
from app.player_list import PlayerList
from app.player import Player


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        """
        Sets up the necessary objects for Player and PlayerList to be used in testing.

        This method initializes players and player lists, preparing them for further
        tests. It ensures that the Player and PlayerList entities are correctly instantiated
        and connected for operations within a testing environment.

        Attributes
        ----------
        my_player_00 : Player
            Player object with ID "1" and name "Marcos".
        my_player_01 : Player
            Player object with ID "2" and name "Socram".
        my_player_02 : Player
            Player object with ID "3" and name "Cosmar".
        my_list : PlayerList
            An initialized, empty PlayerList to be used in tests.
        my_list_test_delete : PlayerList
            A PlayerList pre-populated with `my_player_00` and `my_player_01` for
            testing delete-related functionality.
        """
        self.my_player_00 = Player('1', 'Marcos')
        self.my_player_01 = Player('2', 'Socram')
        self.my_player_02 = Player('3', 'Cosmar')
        self.my_list = PlayerList()
        self.my_list_test_delete = PlayerList()
        self.my_list_test_delete.append(self.my_player_00)
        self.my_list_test_delete.append(self.my_player_01)


    def test_is_empty(self):
        self.assertEqual(self.my_list.is_empty, True)


    def test_append_empty_list(self):
        self.my_list.append(self.my_player_00)
        self.assertFalse(self.my_list.is_empty)


    def test_append_not_empty_list(self):
        """
        Tests the functionality of appending elements to a non-empty list.

        This test ensures that when elements are appended to a non-empty list,
        the list correctly updates its structure such that the `next_player`
        attribute of the second-to-last element is properly assigned, and the
        `next_player` attribute of the last element remains `None`.

        Raises
        ------
        AssertionError
            If the `next_player` attribute of the second-to-last element
            is not properly assigned, or if the `next_player` attribute of
            the last element is not `None`.
        """
        self.my_list.append(self.my_player_00)
        self.my_list.append(self.my_player_01)
        self.assertIsNotNone(self.my_list._head.next_player)
        self.assertIsNone(self.my_list._tail.next_player)


    def test_prepend_head(self):
        """
        Test the prepend functionality of the list.

        This method verifies that the prepend operation correctly adds
        entries to the front of the list, updating links between the nodes
        as expected.

        Attributes
        ----------
        None

        Methods
        -------
        test_prepend_head():
            Tests the prepend functionality by adding elements to the head
            and verifying correct link updates within the list.

        Tests
        -----
        - Ensures the first element is linked properly to the next element.
        - Validates that the head's previous pointer remains None when an
          element is prepended.
        """
        self.my_list.prepend(self.my_player_00)
        self.my_list.prepend(self.my_player_01)
        self.assertEqual(self.my_list._head.next_player.player, self.my_player_00)
        self.assertIsNone(self.my_list._head.previous_player)

    def test_delete_head(self):
        """
        Deletes the head node of the list and performs necessary cleanup to ensure
        the list remains consistent without references to the previous or next
        node from the head.

        Raises
        ------
        AssertionError
            Raised if the expected head node connections are not properly
            updated after deletion and/or the player object associated with
            the head is incorrect.
        """
        self.my_list_test_delete.delete_head()
        self.assertIsNone(self.my_list_test_delete._head.previous_player)
        self.assertIsNone(self.my_list_test_delete._head.next_player)
        self.assertEqual(self.my_list_test_delete._head.player, self.my_player_01)

    def test_delete_tail(self):
        """
        Tests the `delete_tail` method to ensure the correct removal and update of the tail node
        in a doubly linked list.

        This test case method performs multiple assertions to validate that the tail of the
        doubly linked list is deleted appropriately. It ensures that the linked list has its
        references updated correctly, the deleted tail has its pointers cleared, and the
        head and tail are consistent after the deletion.

        Tests:
            - Verifies if the `previous_player` reference of the tail is cleared after deletion.
            - Verifies if the `next_player` reference of the tail is cleared after deletion.
            - Confirms that the head and tail nodes are the same when a single node remains in
              the list.
            - Validates that `player` attribute of the updated tail matches expectations.
        """
        self.my_list_test_delete.delete_tail()
        self.assertIsNone(self.my_list_test_delete._tail.previous_player)
        self.assertIsNone(self.my_list_test_delete._tail.next_player)
        self.assertEqual(self.my_list_test_delete._head, self.my_list_test_delete._tail)
        self.assertEqual(self.my_list_test_delete._tail.player, self.my_player_00)

    def test_delete_key(self):
        """
        Tests the deletion of a key from a custom list structure and ensures the list's
        internal consistency after removal.

        The method validates that a specific player ('2') is deleted successfully and
        verifies that the resulting structure of the linked entities (head, tail,
        previous_player, and next_player) maintains expected references.

        Parameters
        ----------
        self : object
            Instance of the current test class containing attributes for the test
            list (`my_list_test_delete`) and player objects (`my_player_00`, `my_player_02`).

        Raises
        ------
        AssertionError
            If the linked list's internal structure after key deletion does not maintain
            the correct references or order of elements.
        """
        self.my_list_test_delete.append(self.my_player_02)
        self.my_list_test_delete.delete_key('2')
        self.assertEqual(self.my_list_test_delete._head.player, self.my_player_00)
        self.assertEqual(self.my_list_test_delete._tail.player, self.my_player_02)
        self.assertEqual(self.my_list_test_delete._head.next_player.player, self.my_player_02)
        self.assertIsNone(self.my_list_test_delete._head.previous_player)
        self.assertEqual(self.my_list_test_delete._tail.previous_player.player, self.my_player_00)
        self.assertIsNone(self.my_list_test_delete._tail.next_player)
