"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

goods_structure = ("item_name", "price", "qty", "qty_type")
_del = input("Enter the delimiter to split the list values: ")
d = {}
s = ()
u = 1
data = []
while True:
    _list = input(f"Enter data ({goods_structure[0]}, {goods_structure[1]}, {goods_structure[2]}, {goods_structure[3]}) using '{_del}' symbol as the delimiter. Enter Q to stop.\n")
    if _list in "Q":
        break
    elif _del not in _list:
        print("Please use delimiter. Try again.")
    elif len(_list.split(_del)) != 4:
        print("Wrong positions qty. Must be 4. Try again.")
    elif not _list.split(_del)[1].isnumeric() or not _list.split(_del)[2].isnumeric():
        print("Price or Qty must be numeric. Try again.")
    else:
        h = 0
        while h <= 3:
            for p in goods_structure:
                d[p] = _list.split(_del)[h]
                h += 1
        s = (u, d)
        data.append(s)
        u += 1
print(f'\nData structure:\n{data}\n')

# data = [(1, {'item_name': 'comp', 'price': '100', 'qty': '2', 'qty_type': 'sht'}), (2, {'item_name': 'printer', 'price': '200', 'qty': '1', 'qty_type': 'sht'}), (3, {'item_name': 'water', 'price': '5', 'qty': '100', 'qty_type': 'liter'})]

analysis = {}
di_arr = []
for t in range(len(data)):
    di_arr.append(data[t][1])
for key in goods_structure:
    arr_val = []
    for k in range(len(di_arr)):
        arr_val.append(di_arr[k][key])
    analysis[key] = arr_val
print(f"Analytic's data:\n{analysis}")
