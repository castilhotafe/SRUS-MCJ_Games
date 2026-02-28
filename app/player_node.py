


class PlayerNode:
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
        self._next = next_player_node


    def set_previous(self, previous_player_node):
        self._previous = previous_player_node


    def __str__(self):
        return (f'PlayerNode:\n'
                f' key: {self.node_key} - {self.player}')