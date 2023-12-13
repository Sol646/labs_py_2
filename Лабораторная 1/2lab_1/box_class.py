class Box:
    def __init__(self, length: float, width: float):
        """
        Создание коробки

        :param length: Длинна коробки
        :param width: Ширина коробки

        >>> small_box = Box(5.5, 3)
        """
        if not isinstance(length, float):
            raise TypeError("Length has to be float")
        if not isinstance(width, float):
            raise TypeError("Width has to be float")
        self.length = length
        self.width = width
        self.items = []

    def put_item(self, item: str) -> None:
        """
        Положить предмет в коробку

        :param item: Предмет, который кладем в коробку

        >>> small_box.put_item("Кирпич")
        """
        if not isinstance(item, str):
            raise TypeError("Items have to be str")
        ...

    def remove_item(self, item: str) -> None:
        """
        Убрать предмет из коробки

        :param item: Предмет, который достаём из коробку

        >>> small_box.remove_item("Кирпич")
        """
        if not isinstance(item, str):
            raise TypeError("Items have to be str")
        ...

    def print_items(self) -> None:
        """
        Вывести на экран все предметы в коробке
        """
        ...


if __name__ == '__main__':
    import doctest

    doctest.testmod()
