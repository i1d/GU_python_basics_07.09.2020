"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def div_func(a, b):
    """Function for dividing one number by another.

    :param a: float
    :param b: float
    :return: float or inf
    """

#    a = float(input("Enter first value: "))
#    b = float(input("Enter second value: "))
    return a / b if b != 0 else float("inf")


print(div_func(float(input("Enter first value: ")), float(input("Enter second value: "))))
