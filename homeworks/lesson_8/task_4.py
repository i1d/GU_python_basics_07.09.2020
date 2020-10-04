"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Warehouse:
  #    _CAPACITY = 100  # примем вместимость склада в условных единицах (по площади, не по весу)
 #   _occupation = 0  # по дефолту склад пуст
    # если останется время - добавить координаты хранения (матрицу)
 #   objects = []

    def __init__(self, capacity):
        self.capacity = capacity
        self.objects = []
        self.space_occupied = 0


class Equipment:
    #   name = ""  # наименование оборудования
    #   price = 0.0  # цена
    #   unit_size = 0  # сколько места займет на складе в условных единицах
    #   weight = 0  # вес оборудования

    def __init__(self, name: str, price: float, unit_size: int, weight: float):
        self.unit_name = name
        self.unit_price = price
        self.unit_size = unit_size
        self.unit_weight = weight


class Printer(Equipment):
    #   ppm = 0  # производительность стр/мин

    def __init__(self, name, price, unit_size, weight, ppm: int):
        super().__init__(name, price, unit_size, weight)
        self.ppm = ppm


class Scanner(Equipment):
    #   dpi = 0  # качество изображения

    def __init__(self, name, price, unit_size, weight, dpi: int):
        super().__init__(name, price, unit_size, weight)
        self.dpi = dpi


class Xerox(Equipment):
    #    ppm = 0
    #    dpi = 0
    #    brochure_maker = False  # по дефолту брошюровщика нет

    def __init__(self, name, price, unit_size, weight, ppm: int, dpi: int, brochure_maker: bool):
        super().__init__(name, price, unit_size, weight)
        self.ppm = ppm
        self.dpi = dpi
        self.brochure_maker = brochure_maker


if __name__ == '__main__':  # make some tests here to check the objects
    p = Printer("a_printer", 10000.13, 2, 53.1, 100)
    print(vars(p))  # returns a dictionary

    s = Scanner("a_scanner", 29999.99, 3, 89.9, 1200)
    print(vars(s))

    x = Xerox("a_xerox", 80000, 4, 125, 300, 1200, True)
    print(vars(x))
