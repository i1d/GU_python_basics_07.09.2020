"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
import random

random.seed()
my_list = []
for i in range(1, random.randint(5, 10)):
    my_list.append(random.randint(1, 100))
print(f'random_list: {my_list}')


def sort(_list):
    i = 0
    k = 0
    while k <= len(_list) - 1:
        i = k
        while i < len(_list) - 1:
            if _list[i + 1] > _list[k]:
                _list[i + 1], _list[k] = _list[k], _list[i + 1]
            i += 1
        k += 1


sort(my_list)
print(f'sorted_list: {my_list}')
while True:
    u_val = input("Enter int: ")
    if not u_val.isnumeric():
        print("Enter int, not string. Try again")
    else:
        u_val = int(u_val)
        break
k = 0
while k <= len(my_list) - 1:
    if u_val > my_list[k]:
        my_list.insert(k, u_val)
        print(f"> inserted {u_val} into {my_list} on {k}'th index")
        break
    k += 1
if u_val <= my_list[-1]:  # не нравится это решение, ибо выглядит как адский костыль, но по-другому пока не придумал :(
    my_list.append(u_val)
    print(f"< inserted {u_val} into {my_list} as last element")
print(f'new_list: {my_list}')
