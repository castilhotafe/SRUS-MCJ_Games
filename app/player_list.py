
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


    def delete_head(self):
        if self.is_empty:
            raise Exception("List is empty.")
        if self._head.next_player is None:
            self._head = self._tail = None
        else:
            self._head = self._head.next_player
            self._head.set_previous(None)


    def delete_tail(self):
        if self.is_empty:
            raise Exception("List is empty")
        if self._head.next_player is None:
            self._head = self._tail = None
        else:
            self._tail = self._tail.previous_player
            self._tail.set_next(None)
