"""Defines the PlayerList class, which implements a doubly linked list for managing player data.

This module provides the PlayerList class with methods to perform operations such as appending,
prepending, deleting by position (head/tail), deleting by key, and displaying the list contents.
PlayerList uses PlayerNode objects as its nodes and supports traversing the list in both
forward and reverse directions.

The PlayerList operates as a dynamic data structure suitable for representing sequential data
with efficient insertions and deletions.
"""
from app.player_node import PlayerNode
from app.player import Player


class PlayerList:
    """
    Represents a doubly linked list with functionalities to manage, traverse,
    and modify a list of players.

    This class provides methods to append, prepend, and delete nodes with
    specified keys, as well as to traverse the list in both directions.

    Attributes
    ----------
    is_empty : bool
        Indicates whether the list is empty.
    """

    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def is_empty(self):
        """
        Check if the data structure is empty.

        Returns
        -------
        bool
            True if the data structure is empty, False otherwise.
        """
        return self._head is None and self._tail is None

    def append(self, data):
        """
        Appends a new node with the given data to the end of the list.

        Parameters
        ----------
        data : Any
            The data to be stored in the new node.
        """
        new_node = PlayerNode(data)
        if self.is_empty:
            self._head = self._tail = new_node
        else:
            self._tail.set_next(new_node)  # Current tail gives its hand to the new node
            new_node.set_previous(self._tail)  # New node recognizes who was holding the end of the list
            # Move the tail pointer so the list still knows its last element
            self._tail = new_node

    def prepend(self, data):
        """
        Prepends a new node containing the specified data to the beginning of the
        list. Updates the head pointer to the new node. If the list is empty,
        sets both head and tail to the new node.

        Parameters
        ----------
        data : Any
            The data to be stored in the new node.
        """
        new_node = PlayerNode(data)
        if self.is_empty:
            self._head = self._tail = new_node
        else:
            self._head.set_previous(new_node)  # Old head gives hand back to new node
            new_node.set_next(self._head)  # new node gives front hand to the head node
            # head points to the new node
            self._head = new_node

    def delete_head(self):
        """
        Removes the head element from the list. If the list is empty, an exception
        will be raised. If there is only one element in the list, it resets both
        the head and tail to `None`. Otherwise, it updates the head to the next
        player and sets the `previous` reference of the new head to `None`.

        Raises
        ------
        Exception
            If the list is empty.
        """
        if self.is_empty:
            raise Exception("List is empty.")
        if self._head.next_player is None:
            self._head = self._tail = None
        else:
            self._head = self._head.next_player
            self._head.set_previous(None)

    def delete_tail(self):
        """
        Deletes the tail element from the list.

        This method removes the last element of the list. If the list is empty, an
        exception is raised. If the list contains only one element, the list is reset
        to an empty state. Otherwise, the tail pointer is moved to the previous element,
        and its `next` reference is set to None.

        Raises
        ------
        Exception
            If the list is empty.
        """
        if self.is_empty:
            raise Exception("List is empty")
        if self._head.next_player is None:
            self._head = self._tail = None
        else:
            self._tail = self._tail.previous_player  # Update pointer to previous node
            self._tail.set_next(None)  # let go the old tail

    def delete_key(self, key):
        """
        Deletes a node from the list based on the provided key. It ensures proper update of
        linked nodes and handles edge cases when the key corresponds to the head, tail, or
        non-existent nodes within the list.

        Parameters
        ----------
        key : Any
            The identifier of the node to be deleted.

        Raises
        ------
        Exception
            If the list is empty or the key is not found.
        """
        if self.is_empty:
            raise Exception("List is empty")

        if self._head.next_player is None:
            if self._head.player.uid == key:
                self._head = None
                self._tail = None
                return
            raise Exception("Key not found")

        if self._head.player.uid == key:
            self.delete_head()
            return

        if self._tail.player.uid == key:
            self.delete_tail()
            return

        pointer = self._head.next_player
        while pointer is not None and pointer.player.uid != key:
            pointer = pointer.next_player
        if pointer is None:
            raise Exception("Key not found")

        previous_node = pointer.previous_player
        next_node = pointer.next_player
        previous_node.set_next(next_node)
        if next_node is not None:
            next_node.set_previous(previous_node)

    def display(self, forward=True):
        """
        Displays the elements of a list either in forward or backward direction
        based on the `forward` parameter. If the list is empty, it notifies
        the user.

        Parameters
        ----------
        forward : bool, optional
            Determines the direction of iteration. If `True`, iterates
            from the head to the tail of the list. If `False`, iterates
            from the tail to the head. Defaults to `True`.
        """
        if self.is_empty:
            print("List is empty")
            return
        if forward:
            pointer = self._head
            while pointer is not None:
                print(pointer)
                pointer = pointer.next_player
        else:
            pointer = self._tail
            while pointer is not None:
                print(pointer)
                pointer = pointer.previous_player

    def find_key(self, key: str) -> Player | None:
        if self.is_empty:
            return None

        pointer = self._head
        while pointer is not None:
            if pointer.player.uid == key:
                return pointer.player
            pointer = pointer.next_player

        return None

    def __len__(self):
        list_player_count = 0
        if self.is_empty:
            return list_player_count
        pointer = self._head
        while pointer is not None:
            list_player_count += 1
            pointer = pointer.next_player

        return list_player_count
