import doctest


class Pile:
    def __init__(self, section_length: float, section_width: float, pile_height: float):
        """
        Создание и подготовка к работе объекта "Свая"

        :param section_length: Длина сечения сваи
        :param section_width: Ширина сечения сваи
        :param pile_height: Высота сваи

        Примеры:
        >>> pile = Pile(300, 300, 10000)  # инициализация экземпляра класса
        """
        if not isinstance(section_length, (int, float)):
            raise TypeError("Длина сечения сваи должна быть целым или вещественным числом")
        if section_length <= 0:
            raise ValueError("Длина сечения сваи должна быть положительным числом")
        self.section_length = section_length

        if not isinstance(section_width, (int, float)):
            raise TypeError("Ширина сечения сваи должна быть целым или вещественным числом")
        if section_width <= 0:
            raise ValueError("Ширина сечения сваи должна быть положительным числом")
        self.section_width = section_width

        if not isinstance(pile_height, (int, float)):
            raise TypeError("Высота колонны должна быть целым или вещественным числом")
        if pile_height <= 0:
            raise ValueError("Высота колонны должна быть положительным числом")
        self.pile_height = pile_height

    def height_change(self, cutting_length: float) -> None:
        """
        Функция изменения высоты сваи.

        :param cutting_length: Длина срезаемой части сваи
        :rise TypeError: Если длина срезаемой части сваи не целое или вещественное число
        :rise ValueError: Если длина срезаемой части сваи не положительное число
        :rise ValueError: Если длина срезаемой части сваи больше длины сваи

        :return: Высота сваи полсе обрезки

        Примеры:
        >>> pile = Pile(300, 300, 10000)
        >>> pile.height_change(500)
        """
        ...

    def section_length_change(self, added_width: float) -> None:
        """
        Функция увеличивает ширину сечения сваи.

        :param added_width: Добавленная ширина сечения сваи
        :rise TypeError: Если добавленная ширина не целое или вещественное число
        :rise ValueError: Если добавленная ширина не положительное число

        :return: Ширина сечения сваи после увеличения

        Примеры:
        >>> pile = Pile(300, 300, 10000)
        >>> pile.section_length_change(100)
        """
        ...


class Crane:
    def __init__(self, boom_reach: float, lifting_speed: float):
        """
        Создание и подготовка к работе объекта "Подъемный кран"

        :param boom_reach: Вылет стрелы
        :param lifting_speed: Скорость поднимания/опускания

        Примеры:
        >>> crane = Crane(40, 100)  # инициализация экземпляра класса
        """
        if not isinstance(boom_reach, (int, float)):
            raise TypeError("Вылет стрелы должен быть целым или вещественным числом")
        if boom_reach <= 0:
            raise ValueError("Вылет стрелы должен быть положительным числом")
        self.boom_reach = boom_reach

        if not isinstance(lifting_speed, (int, float)):
            raise TypeError("Скорость поднимания/опускания должна быть целым или вещественным числом")
        if lifting_speed <= 0:
            raise ValueError("Скорость поднимания/пускания должна быть положительным числом")
        self.lifting_speed = lifting_speed

    def is_lifting_speed_allowed(self) -> bool:
        """
        Функция которая проверяет является ли скорость допустимой
        if lifting_speed < 100:
            raise ValueError("Скорость подъема/опускания должна быть больше 100")

        :return: Является ли скорость допустимой

        Примеры:
        >>> crane = Crane(40, 60)
        >>> crane.is_lifting_speed_allowed()
        """
        ...

    def luffing_out(self, reduction_amount: float) -> None:
        """
        Уменьшение вылета стрелы.
        :param reduction_amount: Величина уменьшения
        :raise ValueError: Если вылет уменьшается на значение, превышающее максимальный вылет стрелы

        :return: Величина реального изменения вылета

        Примеры:
        >>> crane = Crane(40, 60)
        >>> crane.luffing_out(5)
        """
        ...


class Bucket:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Бадья"

        :param capacity_volume: Объем бадьи
        :param occupied_volume: Объем бетонной смеси

        Примеры:
        >>> bucket = Bucket(3, 2)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем бадьи должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем бадьи должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объем бетонной смеси должен быть типа int или float")
        if occupied_volume <= 0:
            raise ValueError("Объем бетонной смеси должен быть положительным числом")
        self.occupied_volume = occupied_volume

    def is_empty_bucket(self) -> bool:
        """
        Функция которая проверяет является ли бадья пустой

        :return: Является ли бадья пустой

        Примеры:
        >>> bucket = Bucket(3, 1)
        >>> bucket.is_empty_bucket()
        """
        ...

    def add_concrete_to_bucket(self, concrete: float) -> None:
        """
        Добавление бетонной смеси в бадью.
        :param concrete: Объем добавляемой бетонной смеси
        :raise ValueError: Если объем добавляемой бетонной смеси превышает свободное место в бадье, то вызываем ошибку

        :return: Объем реально добавленной бетонной смеси

        Примеры:
        >>> bucket = Bucket(3, 1)
        >>> bucket.add_concrete_to_bucket(1)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в докуменатции
    pass
