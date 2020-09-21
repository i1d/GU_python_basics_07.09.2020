"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def mult(a, b):
    return a * b


# 1
lst_1 = [val for val in range(100, 1001) if val % 2 == 0]
r_1 = reduce(lambda a, b: a * b, lst_1)
print(r_1)

# 2
lst_2 = [val for val in range(100, 1001)][0::2]
r_2 = reduce(mult, lst_2)
print(r_2)

# 3
lst_3 = []
i = 100
while i < 1001:
    lst_3.append(i)
    i += 2
r_3 = 1
for item in lst_3:
    r_3 *= item
print(r_3)

assert lst_1 == lst_2 == lst_3, "check lists"
assert r_1 == r_2 == r_3, "check multiplication result"
