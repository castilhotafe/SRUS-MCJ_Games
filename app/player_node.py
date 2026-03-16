"""
Represents a node in a doubly-linked list structure, specifically designed
for holding player data.

This class is used to manage players in a relationship-based structure,
where each node maintains information about its associated player,
as well as links to the next and previous nodes in the list.
"""


class PlayerNode:
    """
    Represents a node in a doubly linked list structure specifically designed for player objects.

    This class encapsulates a `player` object and maintains references to the next and
    previous nodes, enabling traversal in both directions. It provides properties for
    accessing essential attributes and methods for maintaining the links between nodes.

    Attributes
    ----------
    player : any
        The player object encapsulated within the node.
    next_player : PlayerNode or None
        The next node in the linked list, or None if it is the last node.
    previous_player : PlayerNode or None
        The previous node in the linked list, or None if it is the first node.
    node_key : any
        A unique key that identifies the player object within the node. Typically derived
        from the player's unique identifier.
    """

    def __init__(self, player):
        self._player = player
        self._next = None
        self._previous = None

    @property
    def player(self):
        return self._player

    @property
    def next_player(self):
        return self._next

    @property
    def previous_player(self):
        return self._previous

    @property
    def node_key(self):
        return self._player.uid

    def set_next(self, next_player_node):
        """
        Sets the next player node in the sequence.

        This method updates the internal pointer to reference the next player node in
        the linked sequence of nodes, facilitating ordered traversal or processing
        of players.

        Parameters
        ----------
        next_player_node
            The node representing the next player in the sequence.
        """
        self._next = next_player_node

    def set_previous(self, previous_player_node):
        """
        Sets the previous node for a player node in a linked structure. This method
        assigns the provided node as the previous node, allowing the construction
        or modification of linked structures.

        Parameters
        ----------
        previous_player_node : Node
            The node to be set as the previous node of the current player node.
        """
        self._previous = previous_player_node

    def __str__(self):
        return (f'PlayerNode:\n'
                f' key: {self.node_key} - {self.player}')
