class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.houses_history.append(name)

    def go_to(self, new_floor):  # номер этажа, на который нужно приехать
        for i in range(1, new_floor + 1):
            if new_floor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break

    def __len__(self):    # возвращает кол-во этажей здания
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):   # возвращает True, если кол-во этажей одинаковое у self и у other
        if self.number_of_floors == other.number_of_floors:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):     # увеличивает кол-во этажей на переданное значение
        self.value = value
        self.number_of_floors += value
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)