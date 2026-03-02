"""
Represents a Player entity with unique identifier and name attributes.

This class provides functionality to represent basic details of a
player, including a unique identifier and name. The attributes are
accessible via read-only properties.
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
    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name


    def __str__(self):
        return f'Player id: {self.uid}\n Name: {self.name}'