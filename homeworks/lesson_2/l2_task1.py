"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
import random

random.seed()
type_list = ["none", "int", "float", "complex", "str", "list", "tuple", "set", "bool", "range", "dict"]
type_set = ["int", "float", "complex", "str", "tuple"]
# Only immutable (and hashable) objects can be a part of a set object.
# Numbers (integer, float, as well as complex), strings, and tuple objects are accepted


def rnd(type_lst):
    _choice = random.choice(type_lst)
    if _choice == "none":
        val = None
    elif _choice == "int":
        val = random.randint(0, 99)
    elif _choice == "str":
        val = []
        for i in range(random.randint(5, 10)):
            val.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        val = "".join(val)
    elif _choice == "float":
        val = random.random()
    elif _choice == "complex":
        val = complex(random.randint(1, 10), random.randint(1, 10))
    elif _choice == "list":
        val = []
        for i in range(random.randint(5, 10)):
            val.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    elif _choice == "tuple":
        val = ()
        for i in range(random.randint(2, 4)):
            val += (rnd(type_lst), )
    elif _choice == "set":
        val = set()
        for i in range(random.randint(2, 4)):
            val.add(rnd(type_set))
    elif _choice == "bool":
        val = bool(random.choice([0, 1]))
    elif _choice == "range":
        val = range(random.randint(0, 99))
    elif _choice == "dict":
        val = {}
        for i in range(random.randint(2, 4)):
            val[i] = rnd(type_lst)
    return val


_list = []
for i in range(random.randint(len(type_list), len(type_list) * 2)):
    _list.append(rnd(type_list))
print(f'List with {len(_list)} items:')
print(_list)
class_len = []
for item in _list:
    class_len.append(len(str(type(item))))
max_class_len = max(class_len)
print()
print("List items with their types:")
for item in _list:
    print(f'    {type(item)};{" " * (max_class_len - len(str(type(item))))} value: {item}')
