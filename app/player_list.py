
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

    def delete_key(self, key):
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



