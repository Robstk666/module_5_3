class House:
    def __init__(self, name, floors):
        """
        Конструктор класса House. Инициализирует дом с названием и количеством этажей.
        """
        self.name = name
        self.floors = floors

    def __str__(self):
        """
        Специальный метод для строкового представления объекта.
        """
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def __eq__(self, other):
        """
        Сравнение на равенство по количеству этажей.
        """
        if isinstance(other, House):
            return self.floors == other.floors
        return False

    def __lt__(self, other):
        """
        Оператор меньше (<). Сравнивает количество этажей.
        """
        if isinstance(other, House):
            return self.floors < other.floors
        return False

    def __le__(self, other):
        """
        Оператор меньше или равно (<=). Сравнивает количество этажей.
        """
        if isinstance(other, House):
            return self.floors <= other.floors
        return False

    def __gt__(self, other):
        """
        Оператор больше (>). Сравнивает количество этажей.
        """
        if isinstance(other, House):
            return self.floors > other.floors
        return False

    def __ge__(self, other):
        """
        Оператор больше или равно (>=). Сравнивает количество этажей.
        """
        if isinstance(other, House):
            return self.floors >= other.floors
        return False

    def __ne__(self, other):
        """
        Оператор неравенства (!=). Сравнивает количество этажей.
        """
        if isinstance(other, House):
            return self.floors != other.floors
        return False

    def __add__(self, value):
        """
        Оператор сложения (+). Увеличивает количество этажей на переданное значение.
        """
        if isinstance(value, int):
            self.floors += value
            return self
        return NotImplemented

    def __radd__(self, value):
        """
        Оператор обратного сложения (допускает выражение вида 10 + дом).
        """
        return self.__add__(value)

    def __iadd__(self, value):
        """
        Оператор +=. Увеличивает количество этажей на переданное значение.
        """
        return self.__add__(value)


# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)


print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)