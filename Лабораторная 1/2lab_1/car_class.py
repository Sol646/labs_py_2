class Car:
    def __init__(self, brand: str, color: str, type: str):
        """
        Краткое описание машины

        :param brand: Марка
        :param color: Цвет
        :param type: Тип (седан, универсал и тд)

        >>> mothers_car = Car("Toyota", "Красный", "Седан")
        """
        if not isinstance(brand, str):
            raise TypeError("Brand has to be str")
        if not isinstance(color, str):
            raise TypeError("Color has to be str")
        if not isinstance(type, str):
            raise TypeError("Type has to be str")
        self.brand = brand
        self.color = color
        self.type = type

    def change_color(self, new_color: str) -> None:
        """
        Перекрасить машину

        :param new_color: Цвет

        >>> mothers_car.change_color("Синий")
        """
        if not isinstance(new_color, str) or new_color == self.color:
            raise TypeError("You cant use this color")
        ...

    def print_params(self) -> None:
        """
        Вывести на экран характеристики машины

        >>> mothers_car.print_params()
        """
        ...


if __name__ == '__main__':
    import doctest

    doctest.testmod()
