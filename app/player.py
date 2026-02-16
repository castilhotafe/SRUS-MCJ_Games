class Player:
    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name

    def __str__(self):
        return f'Player id: {self._uid} -  {self._name}'