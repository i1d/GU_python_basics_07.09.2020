"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a: float, b: float, c: float):
    """Function to compute two biggest arguments (numbers!) and return their sum."""

    try:
        if

    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    elif c > a and c > b:
        max = c

    if b < a < c or c < a < b:
        mid = a
    elif a < b < c or c < b < a:
        mid = b
    elif a < c < b or b < c < a:
        mid = c

    # working with boundary conditions
    if a == b and a > c:
        max = mid = a
    elif a == c and a > b:
        max = mid = a
    elif b == c and b > a:
        max = mid = b
    if a == b == c:
        max = mid = a
    return max + mid


print(my_func("a", "b", 5))
