"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

import random

random.seed()


class DateError(Exception):
    def __init__(self, text):
        self.text = text


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def convert(cls, date: str) -> int:
        date_split = date.split("-")
        d = []
        try:
            if len(date_split) < 3 or len(date_split) > 6:
                raise DateError("Wrong format. Unable to convert.")
        except DateError as err:
            print(err)
        else:
            ind = 0
            while ind <= len(date_split) - 1:
                if len(date_split[ind]) > 0:
                    d.append(date_split[ind])
                else:
                    ind += 1
                    d.append("-" + date_split[ind])
                ind += 1

        try:
            date_int = list(map(int, d))
        except ValueError:
            print("Wrong format. Day / month / year must be a number.")
            date_int= []
        return cls(date_int)

    @staticmethod
    def validate(date):
        try:
            day, month, year = date[0], date[1], date[2]
        except IndexError:
            print(f'Wrong format. Unable to validate.')
        else:
            # проверим год на високосность
            # 0-не високосный год, 1 - високосный год
            if year % 400 == 0:
                bis_sextus = 1
            elif year % 100 == 0:
                bis_sextus = 0
            elif year % 4 == 0:
                bis_sextus = 1
            else:
                bis_sextus = 0

            try:
                if month == 2:
                    if bis_sextus == 0:
                        if day > 28:
                            raise DateError(f"Wrong day for february (must be <= 28 in the non-leap year). Your day={day}.")
                    elif bis_sextus == 1:
                        if day > 29:
                            raise DateError(f"Wrong day for february (must be <= 29 in the leap year). Your day={day}.")
                elif month in (1, 3, 5, 7, 8, 10, 12):
                    if day > 31:
                        raise DateError(f"Wrong day for this ({month}) month (must be <= 31). Your day={day}.")
                elif month in (4, 6, 9, 11):
                    if day > 30:
                        raise DateError(f"Wrong day for this ({month}) month (must be <= 30). Your day={day}.")
                if day < 1:
                    raise DateError(f"Wrong day (must be >= 1). Your day={day}.")
                elif not 1 <= month <= 12:
                    raise DateError(f"Wrong month (must be between 1 and 12). Your month={month}.")
            except DateError as err:
                print(err)
            else:
                bc = ""
                if year < 0:
                    bc = " B.C."
                print(f"Date '{day:>2}.{month:>2}.{abs(year):>4}'{bc} is valid.")


print("Press 'return' to continue or 'q' for exit.")
i = ""
while i != "q":
    d = random.randint(-1, 35)
    m = random.randint(-1, 15)
    y = random.randint(-10000, 10000)
    dt = f'{d}-{m}-{y}'
    print(dt)
    date_input = Date.convert(dt)
    Date.validate(date_input.date)
    i = input().lower()

