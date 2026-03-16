"""
A hash map implementation to store and manage Player objects.

This module provides a hash-map-like structure tailored for the storage,
retrieval, and manipulation of Player objects using their keys. Internally,
it leverages PlayerList for each bucket to handle potential hash collisions.
"""

from app.player_list import PlayerList
from app.player import Player


class PlayerHashMap:
    """
    Class for managing a hashmap of Player objects.

    This class is designed to map player keys (either strings or Player objects)
    to their corresponding Player instances using a fixed-size hashmap structure.
    Each index in the hashmap contains a PlayerList, which stores players. The class
    supports CRUD operations and provides utility methods to manage the players
    efficiently.

    Attributes
    ----------
    hashmap : list of PlayerList
        The core structure of the PlayerHashMap, which consists of multiple PlayerList objects to store players.
    """

    def __init__(self):
        self.__SIZE: int = 10
        self.hashmap = []
        for _ in range(self.__SIZE):
            self.hashmap.append(PlayerList())

    def get_index(self, key: str | Player) -> int:
        """
        Gets the index associated with a given key, which can be either a `Player` object or a string,
        by hashing the key and deriving its position in a fixed-size data structure.

        Parameters
        ----------
        key : str or Player
            The key whose index is to be calculated. It can either be a `Player` instance or a string.

        Returns
        -------
        int
            The computed index for the given key.
        """
        if isinstance(key, Player):
            return hash(key) % self.__SIZE
        else:
            return Player.hash(key) % self.__SIZE

    def __getitem__(self, key) -> Player | None:
        """
        Retrieve a player using the given key from the PlayerList.

        Searches for a player in the appropriate PlayerList, determined by hashing
        the key, and retrieves the corresponding Player object if it exists. If the
        player does not exist, a KeyError is raised.

        Parameters
        ----------
        key
            The key used to locate the corresponding Player object.

        Returns
        -------
        Player or None
            The Player object associated with the given key if it exists.

        Raises
        ------
        KeyError
            If no player exists for the provided key.
        """
        player_list: PlayerList = self.hashmap[self.get_index(key)]
        player: Player | None = player_list.find_key(key)
        if player is None:
            raise KeyError(f"{key} Does not exist")
        return player

    def __setitem__(self, key: str, name: str) -> None:
        """
        Sets a player's name in the PlayerList. If the player does not exist in the list,
        a new player is created and added to the list. Otherwise, the name of the existing
        player is updated.

        Parameters
        ----------
        key : str
            The unique identifier for the player.
        name : str
            The name to associate with the player.

        Returns
        -------
        None
            This implementation does not return any value.
        """
        # get the player's appropriate PlayerList:
        player_list = self.hashmap[self.get_index(key)]
        player = player_list.find_key(key)
        # check if the player is in the list
        # If it isn't, create a player and add the player to the player list
        if player is None:
            new_player = Player(key, name)
            player_list.append(new_player)
        else:
            player.name = name

    def __delitem__(self, key):
        """
        Deletes an item from the internal data structure by its key.

        Removes the item corresponding to the provided key from the appropriate
        index in the hashmap.

        Parameters
        ----------
        key
            The key of the item to be deleted.
        """
        player_list = self.hashmap[self.get_index(key)]
        player_list.delete_key(key)

    def __len__(self):
        """
        Calculates the total number of players stored in the hashmap.

        Iterates through the lists of players stored in the hashmap and calculates
        the cumulative count of players by summing up the lengths of the non-empty lists.

        Returns
        -------
        int
            Total number of players in the hashmap.
        """
        total_players_count = 0
        for player_list in self.hashmap:
            if not player_list.is_empty:
                total_players_count += len(player_list)
        return total_players_count

    def display(self):
        """
        Displays the contents of the hashmap.

        Iterates through the hashmap to locate all non-empty lists of players and
        displays their contents. Each list is prefixed by its index in the hashmap.

        """
        for index, player_list in enumerate(self.hashmap):
            if not player_list.is_empty:
                print(f"LIST INDEX: {index}")
                player_list.display()
