"""
References to understand recursion
better and create algorithm for binary search tree:

    GeeksforGeeks:
    https://www.geeksforgeeks.org/dsa/insertion-in-binary-search-tree/

    Medium:
    https://medium.com/@siddharthgupta555t/finally-understanding-recursion-and-binary-search-trees-857c85e72978
"""
from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self, root=None):
        self._root = root

    @property
    def root(self):
        return self._root

    def insert(self, player: Player):
        """
        Insert a Player into the Binary Search Tree.

        This method starts the recursive insertion from the root node and
        ensures that the tree remains connected by assigning the returned
        node back to the root.

        The Player object is inserted using player.name as the key.

        If the tree is empty, the Player becomes the root node.
        If a Player with the same name already exists, that node is updated.

        Parameters
        ----------
        player : Player
            The Player object to insert into the tree.

        Returns
        -------
        None
            The tree is updated in place.
        """
        #start from root and keep tree connected
        self._root = self.insert_recursive(self._root, player)

    def insert_recursive(self, current_node, player: Player):
        """
        Recursively insert a Player into the Binary Search Tree.

        This follows the BST rules:
        - smaller names go to the left subtree
        - greater names go to the right subtree
        - the same name updates the existing node

        The recursion continues until an empty position (None) is found,
        where a new node is created.

        Parameters
        ----------
        current_node : PlayerBNode or None
            The node currently being checked.
        player : Player
            The Player object to insert.

        Returns
        -------
        PlayerBNode
            The current node after insertion, used to keep the tree structure
            connected while recursion returns.
        """

        #base case: empty spot, create node
        if current_node is None:
            return PlayerBNode(player)

        # go left if smaller
        if player.name < current_node.player.name:
            # connect returned subtree back to left
            current_node.left = self.insert_recursive(current_node.left, player)

        #go right if greater
        elif player.name > current_node.player.name:
            # connect returned subtree back to right
            current_node.right = self.insert_recursive(current_node.right, player)

        #same key, update player
        else:
            current_node._player = player

        # return node to keep links correct
        return current_node
