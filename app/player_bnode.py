class PlayerBNode:
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
