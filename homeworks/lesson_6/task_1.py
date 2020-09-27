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

    def running(self):
        print(f"Turning the Traffic Light on.")
        с = 0
        for color in cycle(["Red", "Yellow", "Green"]):
            if с > 10:
                break
            if color == "Red":
                TrafficLight.__color = color
                print_wait(color, 7)
            elif color == "Yellow":
                TrafficLight.__color = color
                print_wait(color, 2)
            elif color == "Green":
                TrafficLight.__color = color
                print_wait(color, random.randint(1, 10))
            с += 1


light = TrafficLight()
light.running()
