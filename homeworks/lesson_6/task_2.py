"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т"""
default_m = 25


class Road:
    _length = 0
    _width = 0

    def weight(self, mass_1cm, thickness):
        mass = self._length * self._width * mass_1cm * thickness
        return mass

    def __init__(self, length, width):
        self._length = length
        self._width = width


l = input("Enter road length in meters: ")
try:
    l = float(l)
except ValueError as err:
    print(f"Sorry, wrong length. Details: {err}")
w = input("Enter road width in meters: ")
try:
    w = float(w)
except ValueError as err:
    print(f"Sorry, wrong width. Details: {err}")
th = input("Enter desired asphalt thickness in CM: ")
try:
    th = float(th)
except ValueError as err:
    print(f"Sorry, wrong thickness. Details: {err}")

try:
    r = Road(l, w)
    m = r.weight(default_m, th)
    print(f'You will need {m:.2f} kg (or {m / 1000:.2f} tons) of asphalt to cover up the road\n'
          f'with lenght={l}m, width={w}m and asphalt thickness={th}cm.\n'
          f'Default asphalt weight to cover 1 square meter = {default_m} kg.')
except TypeError as err:
    print(f"Sorry, seems some value has wrong type. Details: {err}")
