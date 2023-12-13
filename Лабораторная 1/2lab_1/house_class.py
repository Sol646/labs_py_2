class House:
    def __init__(self, rooms: int, floors: int, owner_lastname: str):
        """
        Краткое описание дома

        :param rooms: Кол-во комнат (не больше 20)
        :param floors: Кол-во этажей (не больше 2)
        :param owner_lastname: Фамилия владельца дома

        >>> first_house = House(5, 1, "Растиславов")
        """
        if not isinstance(rooms, int) and 0 < rooms <= 20:
            raise TypeError("Incorrect number of rooms")
        if not isinstance(floors, int) and 0 < floors <= 2:
            raise TypeError("Incorrect number of floors")
        if not isinstance(owner_lastname, str):
            raise TypeError("Lastname has to be str")
        self.rooms = rooms
        self.floors = floors
        self.owner_lastname = owner_lastname

    def change_owner(self, prev: str, new: str) -> None:
        """
        Сменить владельца

        :param prev: Прошлый владелец
        :param new: Новый владелец

        >>> first_house.change_owner("Тарасов", "Басов")
        """
        if not isinstance(prev, str) or not isinstance(new, str):
            raise TypeError("Lastname has to be str")
        ...

    def change_rooms(self, new_rooms: int) -> None:
        """
        Изменить кол-во комнат

        :param new_rooms: Новое кол-во комнат

        >>> first_house.change_rooms(12)
        """
        if not isinstance(rooms, int) and 0 < rooms <= 20:
            raise TypeError("Incorrect number of rooms")
        ...

    def get_current_owner(self) -> str:
        """
        Возвращает текущего владельца

        :return: Фамилия текущего владельца

        >>> first_house.get_current_owner()
        """
        ...


if __name__ == '__main__':
    import doctest

    doctest.testmod()
