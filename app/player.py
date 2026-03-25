"""
Represents a Player entity with unique identifier and name attributes.

This class provides functionality to represent basic details of a
player, including a unique identifier and name.

References:
    https://docs.python.org/3/library/functions.html#property
"""


class Player:
    """
    Represents a player with a unique identifier and a name.

    This class is used for storing and accessing information about a player,
    including their unique ID and their name. It provides properties for
    accessing these attributes and a string representation of the player
    for display purposes.

    Attributes
    ----------
    uid : str
        The unique identifier of the player.
    name : str
        The name of the player.
    """

    def __init__(self, uid: str, name: str, score=0):
        self._uid = uid
        self._name = name
        self._score = score

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    # I have looked up this syntax using python documentation for @property
    # The reference URL is included in the module docstring
    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        if new_score < 0:
            raise ValueError("Score can only be non-negative integers")
        self._score = new_score


    @classmethod
    def hash(cls, key: str) -> int:
        total_value: int = 0
        for char in key:
            total_value += ord(char)
        return total_value

    @classmethod
    def sort_players(cls, player_list):
        if len(player_list) <= 1:
            return player_list
        middle = len(player_list) // 2
        pivot = player_list[middle]
        left = []
        right = []
        equal = []
        for player in player_list:
            if player > pivot:
                left.append(player)
            elif player < pivot:
                right.append(player)
            else:
                equal.append(player)
        return (
            cls.sort_players(left)
            + equal
            + cls.sort_players(right)
        )

    def __hash__(self):
        return self.hash(self.uid)

    def __eq__(self, other):
        return self.uid == other.uid and self.score == other.score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __str__(self):
        return f'Player id: {self.uid}\n Name: {self.name}'

    def __repr__(self):
        return f"{self.__class__.__name__}(name = {self.name}, uid = {self.uid} score = {self.score}"
