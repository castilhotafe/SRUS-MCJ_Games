"""
Binary tree node implementation for PlayerBST.

This module defines the PlayerBNode class, which stores a Player object
and keeps references to the left and right child nodes.

It is used as the basic building block of the Binary Search Tree
structure for Player objects.
"""


class PlayerBNode:
    """
    Node class used by PlayerBST.

    This class stores a Player object and links to the left and right
    child nodes in the Binary Search Tree.
    """

    def __init__(self, player, left=None, right=None):
        self._player = player
        self._left = left
        self._right = right

    @property
    def player(self):
        return self._player

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value
