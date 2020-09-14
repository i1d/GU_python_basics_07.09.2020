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
        for p in goods_structure:
            d[p] = _list.split(_del)[h]
            h += 1
        s = (u, d)
        data.append(s)
        u += 1
print(data)
