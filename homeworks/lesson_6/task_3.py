"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на
реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""


class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f"{self.position}'s total wage = {float(self.income['wage']) + float(self.income['bonus']):.2f}")


w1 = Position(name="Ivan", surname="Ivanov", position="developer", income={"wage": 100000, "bonus": 50000})
print(w1.name, w1.surname, w1.position, w1.income)
w1.get_full_name()
w1.get_total_income()

print("-" * 10)

w2 = Position(name="Petr", surname="Petrov", position="senior developer", income={"wage": 200000, "bonus": 100000})
print(w2.name, w2.surname, w2.position, w2.income)
w2.get_full_name()
w2.get_total_income()

print("-" * 10)

w3 = Position(name="Igor", surname="Igorev", position="teamlead", income={"wage": 210000, "bonus": 110000})
print(w3.name, w3.surname, w3.position, w3.income)
w3.get_full_name()
w3.get_total_income()
