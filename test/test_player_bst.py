"""
Unit tests for validating the functionality of the PlayerBST class.

This module provides a series of test cases to verify the behavior of
PlayerBST insertion. The tests include checks for inserting players into
an empty tree, inserting to the left and right side of the root, and
updating an existing node when the same key already exists.

Classes
-------
TestPlayerBST : unittest.TestCase
    Contains unit tests for the PlayerBST class.
"""

import unittest
from app.player import Player
from app.player_bst import PlayerBST


class TestPlayerBST(unittest.TestCase):
    def setUp(self):
        """
        Sets up the necessary objects for Player and PlayerBST to be used in testing.

        This method initializes Player objects and an empty PlayerBST,
        preparing them for insertion tests.

        Attributes
        ----------
        my_player_00 : Player
            Player object with ID "1" and name "Marcos".
        my_player_01 : Player
            Player object with ID "2" and name "Ana".
        my_player_02 : Player
            Player object with ID "3" and name "Zeca".
        my_player_03 : Player
            Player object with ID "4" and name "Carlos".
        my_player_04 : Player
            Player object with ID "5" and name "Marcos".
        my_bst : PlayerBST
            An initialized, empty PlayerBST to be used in tests.
        """
        self.my_player_00 = Player('1', 'Marcos')
        self.my_player_01 = Player('2', 'Ana')
        self.my_player_02 = Player('3', 'Zeca')
        self.my_player_03 = Player('4', 'Carlos')
        self.my_player_04 = Player('5', 'Marcos')
        self.my_bst = PlayerBST()

    def test_insert_empty_tree(self):
        """
        Tests inserting a player into an empty Binary Search Tree.

        This test ensures that the first inserted player becomes the root
        node of the tree.

        Raises
        ------
        AssertionError
            If the root node is not created correctly after insertion.
        """
        self.my_bst.insert(self.my_player_00)
        self.assertIsNotNone(self.my_bst.root)
        self.assertEqual(self.my_bst.root.player, self.my_player_00)
        self.assertIsNone(self.my_bst.root.left)
        self.assertIsNone(self.my_bst.root.right)

    def test_insert_left_of_root(self):
        """
        Tests inserting a player whose name should be placed to the left of the root.

        This test ensures that a player with a smaller name than the root
        is inserted as the left child.

        Raises
        ------
        AssertionError
            If the player is not inserted correctly on the left side.
        """
        self.my_bst.insert(self.my_player_00)
        self.my_bst.insert(self.my_player_01)
        self.assertIsNotNone(self.my_bst.root.left)
        self.assertEqual(self.my_bst.root.left.player, self.my_player_01)
        self.assertIsNone(self.my_bst.root.right)

    def test_insert_right_of_root(self):
        """
        Tests inserting a player whose name should be placed to the right of the root.

        This test ensures that a player with a greater name than the root
        is inserted as the right child.

        Raises
        ------
        AssertionError
            If the player is not inserted correctly on the right side.
        """
        self.my_bst.insert(self.my_player_00)
        self.my_bst.insert(self.my_player_02)
        self.assertIsNotNone(self.my_bst.root.right)
        self.assertEqual(self.my_bst.root.right.player, self.my_player_02)
        self.assertIsNone(self.my_bst.root.left)

    def test_insert_recursive_left_then_right(self):
        """
        Tests recursive insertion into a deeper position in the tree.

        This test ensures that the insertion continues recursively and places
        the player in the correct position inside the left subtree.

        Raises
        ------
        AssertionError
            If the recursive insertion does not place the player correctly.
        """
        self.my_bst.insert(self.my_player_00)
        self.my_bst.insert(self.my_player_01)
        self.my_bst.insert(self.my_player_03)
        self.assertEqual(self.my_bst.root.player, self.my_player_00)
        self.assertEqual(self.my_bst.root.left.player, self.my_player_01)
        self.assertEqual(self.my_bst.root.left.right.player, self.my_player_03)

    def test_insert_duplicate_name_updates_existing_node(self):
        """
        Tests inserting a player with the same name as an existing node.

        This test ensures that duplicate keys are not added as new nodes.
        Instead, the existing node is updated with the new Player object.

        Raises
        ------
        AssertionError
            If a duplicate node is created instead of updating the existing one.
        """
        self.my_bst.insert(self.my_player_00)
        self.my_bst.insert(self.my_player_04)
        self.assertEqual(self.my_bst.root.player, self.my_player_04)
        self.assertIsNone(self.my_bst.root.left)
        self.assertIsNone(self.my_bst.root.right)