from player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None


    @property
    def is_empty(self):
        return self._head is None and self._tail is None

    def append(self, data):
        new_node = PlayerNode(data)
        if self.is_empty:
            self._head = self._tail= new_node
        else:
            self._tail.set_next(new_node)
            new_node.set_previous(self._tail)
            self._tail = new_node


    def prepend(self, data):
        new_node = PlayerNode(data)
        if self.is_empty:
            self._head = self._tail = new_node
        else:
            self._head.set_previous(new_node)
            new_node.set_next(self._head)
            self._head = new_node
