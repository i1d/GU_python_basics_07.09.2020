"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт."""

from itertools import cycle
from time import sleep
import random

random.seed()


def print_wait(col, time):
    print(col, end=" ")
    t = time
    while t >= 0:
        print(f".{t}", end=" ")
        sleep(1)
        t -= 1
    print()


class TrafficLight:
    __color = ""

    def running_1(self):
        print(f"Turning the Traffic Light on - option 1.")
        с = 0
        for color in cycle(["Red", "Yellow", "Green"]):
            if с >= 9:
                break
            if color == "Red":
                self.__color = color
                print_wait(self.__color, 7)
            elif color == "Yellow":
                self.__color = color
                print_wait(self.__color, 2)
            elif color == "Green":
                self.__color = color
                print_wait(self.__color, random.randint(1, 10))
            с += 1

    def running_2(self):
        print(f'Turning the Traffic Light on - option 2.')
        c = 0
        while c <= 9:
            if not self.__color:
                self.__color = "Red"
            elif self.__color == "Red":
                print_wait(self.__color, 7)
                self.__color = "Yellow"
            elif self.__color == "Yellow":
                print_wait(self.__color, 2)
                self.__color = "Green"
            elif self.__color == "Green":
                print_wait(self.__color, random.randint(1, 10))
                self.__color = "Red"
            c += 1

light1 = TrafficLight()
light1.running_1()

print("*" * 10)

light2 = TrafficLight()
light2.running_2()