class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    def __str__(self):
        return f"{self.name} by {self.author}"


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Pages have to be int")
        if value <= 0:
            raise ValueError("Pages have to be over zero")
        self._pages = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Duration has to be int or float")
        if value <= 0:
            raise ValueError("Duration has to be over zero")
        self._duration = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == '__main__':
    # Создание объектов Book, Paperbook и AudioBook
    book = Book(name="Капитанская Дочка", author="А.С. Пушкин")
    print(book)
    print(repr(book))

    paper_book = PaperBook(name="Мёртвые души", author="Н.В. Гоголь", pages=352)
    print(paper_book)
    print(repr(paper_book))

    paper_book.pages = 320
    print(paper_book)
    print(repr(paper_book))

    audio_book = AudioBook(name="Герой нашего времени", author="М.Ю. Лермонтов", duration=8.5)
    print(audio_book)
    print(repr(audio_book))

    audio_book.duration = 6.6
    print(audio_book)
    print(repr(audio_book))