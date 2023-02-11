class Sport:
    """ Базовый класс "Спорт" """

    def __init__(self, name: str, level: str):
        """
        Подготовка объекта "Спорт"
        :param name: Вид спорта
        :param level: Уровень спортивной подготовки ("нулевой", "средний", "высокий")

        Параметр rating: Спортивный разряд (по умолчанию None).
        При наличии уровня подготовки "высокий" параметр level задается через метод get_sport_rating

        Пример:
        >>> tennis = Sport("Теннис", "нулевой")
        """

        if not isinstance(name, str):
            raise TypeError("Вид спорта должен быть типа str")
        self.name = name

        self._TRAINING_LEVEL = ["нулевой", "средний", "высокий"]
        if not isinstance(level, str):
            raise TypeError("Уровень спортивной подготовки должен быть типа str")
        if level in self._TRAINING_LEVEL:
            self.level = level
        else:
            raise ValueError("Уровень спортивной подготовки должен быть нулевой, средний или высокий")

        self._rating = None  # для метода get_sport_rating
        self._hundred_meter_run = None  # для метода level_indicator
        self._jump_length = None  # для метода level_indicator
        self._press = None  # для метода level_indicator

    def __str__(self) -> str:
        """
        Нестрогое представления экземпляра класса.
        Метод наследуется в классе Skiing и Gymnastics
        Пример:
        >>> tennis = Sport("Теннис", "нулевой")
        >>> tennis.__str__()
        'Спорт: Теннис. Уровень подготовки: нулевой.'
        """
        return f"Спорт: {self.name}. Уровень подготовки: {self.level}."

    def __repr__(self) -> str:
        """
        Вывода валидного Python кода
        Пример:
        >>> tennis = Sport("Теннис", "нулевой")
        >>> tennis.__repr__()
        "Sport(name='Теннис', level='нулевой')"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, level={self.level!r})"

    def get_sport_rating(self, rating: str) -> None:
        """
        Метод для фиксирования достигнутого спортивного разряда
        :param rating: Спортивный разряд.
        Спортивный разряд дается только при наличии уровня "высокий"
        Пример:
        >>> tennis = Sport("Tennis", "высокий")
        >>> tennis.get_sport_rating("Кандидат в МС")
        """
        if not isinstance(rating, str):
            raise TypeError("Спортивный разряд должен быть типа str")
        if self.level == self._TRAINING_LEVEL[-1]:
            self._rating = rating
        else:
            raise ValueError("Спортивный разряд дается только при наличии уровня продвинутый")

    def level_indicator(self, pull_ups_bar: int, long_jump: float, flexibility: float) -> None:
        """
        Личные показатели - ОФП.
        Показатели меняются в зависимости от направления спорта.
        :param pull_ups_bar: Подтягивание на высокой перекладине, кол-во раз
        :param long_jump: Прыжок в длину с места, м
        :param flexibility: Наклон ниже опоры, см

        >>> tennis = Sport("Теннис", "высокий")
        >>> tennis.level_indicator(15, 2.5, 15)
        """
        if not isinstance(pull_ups_bar, int):
            raise TypeError
        if pull_ups_bar <= 0:
            raise ValueError
        self._pull_ups_bar = pull_ups_bar

        if not isinstance(long_jump, float):
            raise TypeError
        if long_jump <= 0:
            raise ValueError
        self._long_jump = long_jump

        if not isinstance(flexibility, int):
            raise TypeError
        if flexibility <= 0:
            raise ValueError
        self._flexibility = flexibility


class Gymnastics(Sport):
    """ Дочерний класс "Гимнастика" """

    def __init__(self, name: str, level: str, inventory: str):
        """
        Подготовка объекта "Гимнастика"
        :param name: Наименование спорта
        :param level: Уровень подготовки
        :param inventory: Спортивный инвентарь
        Пример:
        >>> artistic_gymnastics = Gymnastics("Художественная гимнастика", "высокий", "обруч")
        """
        super().__init__(name, level)
        self.inventory = inventory

        self._score = None  # для метода level_indicator

    def __repr__(self) -> str:
        """
        Метод для вывода валидного Python кода.
        Метод перезаписывается, так как в классе Gymnastics задается новый атрибут: inventory
        Пример:
        >>> artistic_gymnastics = Gymnastics("Художественная гимнастика", "высокий", "обруч")
        >>> artistic_gymnastics.__repr__()
        "Gymnastics(name='Художественная гимнастика', level='высокий', inventory='обруч')"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, level={self.level!r}, inventory={self.inventory!r})"

    def level_indicator(self, score: int) -> None:
        """
        Метод для фиксации личных показателей в виде количества баллов за выступление
        :param score: Количество баллов
        Пример:
        >>> artistic_gymnastics = Gymnastics("Художественная гимнастика", "высокий", "обруч")
        >>> artistic_gymnastics.level_indicator(15)
        """

        if not isinstance(score, int):
            raise TypeError("Количество баллов должно быть типа int")
        if score <= 0:
            raise ValueError("Количество баллов должно быть положительным числом")
        self._score = score


if __name__ == "__main__":
    pass
