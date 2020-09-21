"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
# b
from itertools import count, cycle
import random

random.seed()


def unique_list(_lst):
    u_lst = []
    for i in range(len(_lst)):
        t = [el for el in _lst]
        n = t.pop(i)
        if n not in t:
            u_lst.append(n)
    return u_lst


random_lst = [random.randint(0, 15) for val in range(random.randint(15, 30))]
u_list = unique_list(random_lst)
print(u_list)

cnt = 0
for i in cycle(u_list):
    if cnt >= len(u_list) * 3:
        break
    print(i, end=" ")
    cnt += 1
