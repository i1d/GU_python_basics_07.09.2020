"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
_del = input("Enter the delimiter to split the list values: ")
_list = input(f"Enter list of values using the '{_del}' symbol as the delimiter: ").split(_del)
print(f'Initial list with size={len(_list)}: {_list}')
for i in range(0, len(_list) - 1, 2):
    tmp = _list[i]
    _list[i] = _list[i + 1]
    _list[i + 1] = tmp
print(f'Converted list: {_list}')
