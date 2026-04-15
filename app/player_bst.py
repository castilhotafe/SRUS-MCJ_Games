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
        # start from root and keep tree connected
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

        # base case: empty spot, create node
        if current_node is None:
            return PlayerBNode(player)

        # go left if smaller
        if player.name < current_node.player.name:
            # connect returned subtree back to left
            current_node.left = self.insert_recursive(current_node.left, player)

        # go right if greater
        elif player.name > current_node.player.name:
            # connect returned subtree back to right
            current_node.right = self.insert_recursive(current_node.right, player)

        # same key, update player
        else:
            current_node._player = player

        # return node to keep links correct
        return current_node

    def search(self, name: str):
        """
        Search for a Player in the Binary Search Tree by name.

        This method starts the search from the root node and uses recursion
        to navigate through the tree.

        If the Player is found, the Player object is returned.
        If the name does not exist in the tree, None is returned.

        Parameters
        ----------
        name : str
            The name of the Player to search for.

        Returns
        -------
        Player or None
            The Player object if found, otherwise None.
        """
        return self._search_recursive(self._root, name)

    def _search_recursive(self, current_node, name: str):
        """
        Recursively search for a Player starting from the current node.

        This method follows the Binary Search Tree rules:
        - if the name matches the current node, return the Player
        - if the name is smaller, search the left subtree
        - if the name is greater, search the right subtree

        The recursion continues until the Player is found or a None node is reached.

        Parameters
        ----------
        current_node : PlayerBNode or None
            The node currently being checked.
        name : str
            The name of the Player to search for.

        Returns
        -------
        Player or None
            The Player object if found, otherwise None.
        """

        # base case: not found
        if current_node is None:
            return None

        # found starting from the root
        if name == current_node.player.name:
            return current_node.player

        # go left
        if name < current_node.player.name:
            return self._search_recursive(current_node.left, name)

        # go right
        else:
            return self._search_recursive(current_node.right, name)

    def to_sorted_list(self):
        """
        Convert the Binary Search Tree into a sorted list of Player objects.

        This method performs an in-order traversal of the tree.
        Because the BST is ordered by player.name, the resulting list
        will also be sorted by name.

        A temporary list is created and passed to a recursive helper
        function, which fills the list during traversal.

        Returns
        -------
        list[Player]
            A list of Player objects sorted by name.
        """
        players = []
        # create empty list and pass it to be filled during traversal
        self._in_order(self._root, players)
        return players

    def _in_order(self, node, players):
        """
        Perform an in-order traversal of the BST.

        This method visits nodes in the following order:
        left subtree → current node → right subtree

        The list 'players' is passed as a parameter and is updated
        directly during recursion (no return needed).

        Parameters
        ----------
        node : PlayerBNode or None
            The current node being visited.
        players : list
            The list being filled with Player objects in sorted order.
        """

        #base case reached the end of the branch
        if node is None:
            return

        # go to the left of the subtree
        self._in_order(node.left, players)

        # process current node
        players.append(node.player)

        #go to right subtree
        self._in_order(node.right, players)

    def build_balanced_tree(self, players):
        """
        Build a balanced Binary Search Tree from a sorted list of Player objects.

        This method uses a divide-and-conquer approach:
        - it picks the middle element of the list as the root
        - recursively builds the left subtree from the left half
        - recursively builds the right subtree from the right half

        Because the input list is already sorted, this guarantees
        that the resulting tree is balanced.

        Parameters
        ----------
        players : list[Player]
            A list of Player objects sorted by name.

        Returns
        -------
        PlayerBNode or None
            The root node of the new balanced BST.
        """

        # base case: no elements left
        if not players:
            return None

        # find middle index
        middle_index = len(players) // 2

        # create root node from middle element
        root_node = PlayerBNode(players[middle_index])

        # build left subtree from left half of list
        root_node.left = self.build_balanced_tree(players[:middle_index])

        # build right subtree from right half of list
        root_node.right = self.build_balanced_tree(players[middle_index + 1:])

        # return the root of this subtree
        return root_node

    def balance(self):
        """
        Convert the current Binary Search Tree into a balanced BST.

        This method performs the following steps:
        1. Extract all Player objects into a sorted list using in-order traversal.
        2. Rebuild the tree using the sorted list to create a balanced structure.

        The original tree structure is replaced with the new balanced tree.

        Returns
        -------
        None
            The tree is updated in place.
        """

        # get sorted list from current BST
        players = self.to_sorted_list()

        # rebuild tree as balanced BST
        self._root = self.build_balanced_tree(players)