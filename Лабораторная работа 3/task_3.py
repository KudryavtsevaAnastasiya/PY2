class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        """
        Создание и подготовка к работе объекта "Книга"
        :param name: Название книги
        :param author: Автор книги
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Возвращает название книги. Не позволяет изменять атрибут"""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги. Не позволяет изменять атрибут"""
        return self._author

    def __str__(self):
        """
        Функция. которая возвращает строку формата, где "Название_книги" и "Автор_книги" берутся с помощью
        атрибутов name и author
        :return: Строка с названием книги и автором с помощью атрибута name и author
        """
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        """
        Функция. которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр
        :return: Валидная python строка
        """
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """ Дочерний класс книги. Бумажная книга. """

    def __init__(self, name: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Бумажная книга"
        :param name: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге
        """
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц."""
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """Устанавливает количество страниц, накладывает ограничения по типу и допустимым значениям."""
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

    def __repr__(self):
        """
        Функция. которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр
        :return: Валидная python строка
        """
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):
    """ Дочерний класс книги. Аудио книга."""

    def __init__(self, name: str, author: str, duration: float):
        """
        Создание и подготовка к работе объекта "Аудио книга"
        :param name: Название книги
        :param author: Автор книги
        :param duration: Продолжительность книги
        """
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность книги."""
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        """Устанавливает продолжительность, накладывает ограничения по типу и допустимым значениям."""
        if not isinstance(duration, float):
            raise TypeError("Продолжительность книги должна быть типа float")
        if duration < 0:
            raise ValueError("Продолжительность книги должна быть положительным числом")
        self._duration = duration

    def __repr__(self):
        """
        Функция. которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр
        :return: Валидная python строка
        """
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"


print(Book("Унесенные ветром", "Маргарет Митчелл"))
print(PaperBook("Унесенные ветром", "Маргарет Митчелл", 640))
print(AudioBook("Унесенные ветром", "Маргарет Митчелл", 800))
# Последняя строка