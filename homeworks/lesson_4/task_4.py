"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

r_lst = []
for i in range(len(lst)):
    t = [el for el in lst]
    n = t.pop(i)
    if n not in t:
        r_lst.append(n)

#c_lst = [el[1] for el in [(idx, val) for idx, val in enumerate(lst, 0)]]

print(r_lst)

print("---")
print(f'lst_before={lst}')

#a = [t.pop(i) for t in [el for el in lst]]
#_lst = [(idx, val) for idx, val in enumerate(lst.copy(), 0)]
#lst_2 = [(idx, val) for idx, val in enumerate(lst, 0) if lst.copy().pop(idx) not in lst]
lst_2 = [val for idx, val in enumerate(lst, 0) if [998,999].pop(idx) not in lst]
print(f'lst_2={lst_2}')
#r = lst_2.copy().pop(0)[1]
#print(f'r={r}')
#c_lst_2 = [el[1] for el in [(idx, val) for idx, val in enumerate(lst, 0) if lst.copy().pop(idx) not in lst]]

#print(f'_lst={_ls)t}')
#print(f'lst_2={lst_2}')
#print(f'c_lst_2={c_lst_2}')
print(f'lst_after={lst}')
