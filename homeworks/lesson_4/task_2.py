"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
import random

random.seed()

lst = [random.randint(0, 1000) for val in range(random.randint(10, 20))]
print(f'Original list:  {lst}')

c_lst = []
for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        c_lst.append(lst[i])

c_lst_2 = [el[1] for el in [(idx, val) for idx, val in enumerate(lst[1:], 1) if lst[idx] > lst[idx - 1]]]
assert c_lst == c_lst_2, "Check c_lst_2!"

print(f'Converted list: {c_lst}')
print(f'Another way:    {c_lst_2}')



