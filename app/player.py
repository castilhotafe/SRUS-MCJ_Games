class Player:
    def __init__(self, uid: str, name: str):
        self.__uid = uid
        self.__name = name

    @property
    def uid(self):
        return self.__uid

    @property
    def name(self):
        return self.__name


    def __str__(self):
        return f'Player id: {self.__uid}\n Name:  {self.__name}'