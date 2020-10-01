"""3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке https://pythonworld.ru/osnovy/peregruzka-operatorov.html."""

import random

random.seed()


class Cell:
    def __init__(self, slots):
        self.slots_qty = int(slots)

    def __add__(self, other):  # +
        #self.slots_qty += other.slots_qty
        return Cell(self.slots_qty + other.slots_qty)

    def __sub__(self, other):  # -
        if self.slots_qty > other.slots_qty:
            return Cell(self.slots_qty - other.slots_qty)
        else:
            print("Unable to subtract. Difference is <= 0.")

    def __mul__(self, other):  # *
        return Cell(self.slots_qty * other.slots_qty)

    def __truediv__(self, other):  # /
        #return Cell(round(self.slots_qty / other.slots_qty))
        return self.__floordiv__(other)

    def __floordiv__(self, other):  # //
        return Cell(self.slots_qty // other.slots_qty)

    def make_order(self, qt):
        if qt > 0:
            k = self.slots_qty
            st = ""
            for _ in range(k // qt):
                st += "*" * qt + "\n"
            st += "*" * (k % qt)
            return st
        else:
            return "Parameter should be > 0."


c1 = Cell(random.randint(1, 10))
c2 = Cell(random.randint(1, 10))
print(f'Initial cells slots: c1={c1.slots_qty}; c2={c2.slots_qty}')

c3 = c1 + c2
print(f'Addition: {c3.slots_qty}')

c4 = c1 - c2
try:
    print(f'Subtraction: {c4.slots_qty}')
except AttributeError as err:
    print(f'Difference is <= 0. Unable to substract (new object does not exist). Details: {err}')

c4 = c2 - c1
try:
    print(f'Subtraction: {c4.slots_qty}')
except AttributeError as err:
    print(f'Difference is <= 0. Unable to substract (new object does not exist). Details: {err}')

c5 = c1 * c2
print(f'Multiplication: {c5.slots_qty}')

try:
    c6 = c1 // c2
    print(f'Division //: {c6.slots_qty}')
except TypeError: # использовал костыль, чтобы использовать ошибку при целочисленном делении и отсутствии перегрузки __floordiv__
    c6 = c1 / c2
    print(f'Division /: {c6.slots_qty}')

print("-" * 20)
c7 = Cell(random.randint(0, 20))
ord = random.randint(0, 10)
print(f'Order with cell slots {c7.slots_qty} and order {ord}:\n{c7.make_order(ord)}')
