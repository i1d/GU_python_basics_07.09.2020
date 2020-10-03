"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""


class MyError(Exception):
    def __init__(self, text):
        self.text = text


try:
    a = int(input("Enter dividend: "))
    b = int(input("Enter divider: "))
    if b == 0:
        raise MyError("Divider is zero!")
except MyError as err:
    print(f'{err} The result is infinite.')
except ValueError as err:
    print(f"Not a number. Details: {err}")
else:
    print(f"{a}/{b}={a/b}")
