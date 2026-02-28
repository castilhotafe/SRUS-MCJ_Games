from player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self._head = None


    @property
    def is_empty(self):
        return self._head is None

    def append(self, data):
        new_player = PlayerNode(data)
        if self.is_empty:
            self._head = new_player
        else:
            pointer = self._head
            while pointer.next_player:
                pointer = pointer.next_player
            pointer.set_next(new_player)
            new_player.set_previous(pointer)
