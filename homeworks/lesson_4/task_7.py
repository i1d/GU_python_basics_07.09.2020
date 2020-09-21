"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from functools import reduce


def fact(_n):
    yield 1
    k = 2
    while k <= _n:
        yield reduce(lambda a, b: a * b, range(1, k + 1))
        k += 1


n = input("Enter integer value: ")
try:
    n = int(n)
    c = 1
    for i in fact(n):
        print(f'{c}! = {i}')
        c += 1
except ValueError:
    print("Please input integer value.")
