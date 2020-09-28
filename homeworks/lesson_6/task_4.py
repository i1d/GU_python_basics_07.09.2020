"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
import random

random.seed()

turn_direction = ("right", "left", "forward", "backward")


class Car:
    speed = 0
    color = ""
    name = ""
    is_police = bool

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.direction = ""

    def go(self):
        self.speed = random.randint(1, 100)
        print(f'{self.color} {self.name} started driving.')

    def stop(self):
        self.speed = 0
        print(f'{self.color} {self.name} has stopped.')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.color} {self.name} has turned {self.direction}.')

    def show_speed(self):
        print(f'Current speed of {self.color} {self.name} car is: {self.speed}.')


class TownCar(Car):
    is_police = False

    def __init__(self, color):
        self.color = color
        super().__init__('TOWN_CAR', self.color)

    def show_speed(self):
        print(f'Current speed of {self.color} {self.name} car is: {self.speed}.')
        if self.speed > 60:
            print(f'Current speed is exceeded the limit of 60!!!')


class SportCar(Car):
    is_police = False

    def __init__(self, color):
        self.color = color
        super().__init__('SPORT_CAR', self.color)


class WorkCar(Car):
    is_police = False

    def __init__(self, color):
        self.color = color
        super().__init__('WORK_CAR', self.color)

    def show_speed(self):
        print(f'Current speed of {self.color} {self.name} car is: {self.speed}.')
        if self.speed > 40:
            print(f'Current speed is exceeded the limit of 40!!!')


class PoliceCar(Car):
    Car.is_police = True

    def __init__(self, color):
        self.color = color
        super().__init__('POLICE_CAR', self.color)


town_car_1 = TownCar("black")
print(town_car_1.name, town_car_1.color, "is civil car" if not town_car_1.is_police else "is police car")
town_car_1.show_speed()
town_car_1.go()
town_car_1.show_speed()
town_car_1.turn(random.choice(turn_direction))
print(town_car_1.direction)
town_car_1.show_speed()
town_car_1.stop()
town_car_1.show_speed()

print("-" * 10)

sport_car_1 = SportCar("red")
print(sport_car_1.name, sport_car_1.color, "is civil car" if not town_car_1.is_police else "is police car")
sport_car_1.show_speed()
sport_car_1.go()
sport_car_1.show_speed()
sport_car_1.turn(random.choice(turn_direction))
print(sport_car_1.direction)
sport_car_1.show_speed()
sport_car_1.stop()
sport_car_1.show_speed()

print("-" * 10)

work_car_1 = WorkCar("white")
print(work_car_1.name, work_car_1.color, "is civil car" if not town_car_1.is_police else "is police car")
work_car_1.show_speed()
work_car_1.go()
work_car_1.show_speed()
work_car_1.turn(random.choice(turn_direction))
print(work_car_1.direction)
work_car_1.show_speed()
work_car_1.stop()
work_car_1.show_speed()

print("-" * 10)
police_car_1 = PoliceCar("black")
print(police_car_1.name, police_car_1.color, "is civil car" if not town_car_1.is_police else "is police car")
police_car_1.show_speed()
police_car_1.go()
police_car_1.show_speed()
police_car_1.turn(random.choice(turn_direction))
print(police_car_1.direction)
police_car_1.show_speed()
police_car_1.stop()
police_car_1.show_speed()