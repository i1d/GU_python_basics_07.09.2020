"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod
import random

random.seed()


class Clothes(ABC):

    @abstractmethod
    def consumption(self, amount: float) -> float:
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def consumption(self):
        return self.size / 6.5 + 0.5


class Suite(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def consumption(self):
        return 2 * self.size + 0.3


if __name__ == '__main__':
    c1 = Coat("Пальто", random.randint(0, 10))
    print(f'Fabric consumption for {c1.name} with size {c1.size} is: {c1.consumption:.2f}')

    s1 = Suite("Костюм", random.randint(0, 10))
    print(f'Fabric consumption for {s1.name} with size {s1.size} is: {s1.consumption}')

    s2 = Suite("Пиджак", random.randint(0, 10))
    print(f'Fabric consumption for {s2.name} with size {s2.size} is: {s2.consumption}')
