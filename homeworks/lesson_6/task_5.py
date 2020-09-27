"""5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра."""


class Stationery:
    title = ""

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        Stationery.title = "Ручка"
        print("Отрисовка ручкой.", end=" ")


class Pencil(Stationery):
    def draw(self):
        Stationery.title = "Карандаш"
        print("Отрисовка карандашом.", end=" ")


class Handle(Stationery):
    def draw(self):
        Stationery.title = "Маркер"
        print("Отрисовка маркером.", end=" ")


pen = Pen()
pen.draw()
print(pen.title)

pencil = Pencil()
pencil.draw()
print(pencil.title)

handle = Handle()
handle.draw()
print(handle.title)
