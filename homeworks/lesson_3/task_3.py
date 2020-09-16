"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    """Function to compute two biggest arguments (of equal types) and return their sum."""

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
    if a == b < c:
        max = c
        mid = a
    elif a == c < b:
        max = b
        mid = a
    elif b == c < a:
        max = a
        mid = b
    return max + mid


print(my_func(1, 1, 1))

print(my_func(2, 1, 1))
print(my_func(1, 2, 1))
print(my_func(1, 1, 2))

print(my_func(2, 2, 1))
print(my_func(2, 1, 2))
print(my_func(1, 2, 2))

print(my_func(1, 2, 3))
print(my_func(3, 1, 2))
print(my_func(2, 3, 1))

print(my_func("a", "b", "c"))
