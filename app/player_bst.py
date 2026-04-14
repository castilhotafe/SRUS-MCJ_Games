class PlayerBST:
    def __init__(self, root = None):
        self._root = root

    @property
    def root(self):
        return self._root