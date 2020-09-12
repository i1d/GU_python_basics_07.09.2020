"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
import random

random.seed()
type_list = ["none", "int", "float", "str", "list", "tuple", "set", "bool"]
type_set = ["int", "float", "str", "tuple"]
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
    elif _choice == "list":
        val = []
        for i in range(random.randint(5, 10)):
            val.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    elif _choice == "tuple":
        val = ()
        for i in range(random.randint(1, 3)):
            val += (rnd(type_lst), )
    elif _choice == "set":
        val = set()
        for i in range(random.randint(1, 3)):
            val.add(rnd(type_set))
    elif _choice == "bool":
        val = bool(random.choice([0, 1]))
    return val


for i in range(random.randint(len(type_list), len(type_list) * 2)):
    res = rnd(type_list)
    print(f'{type(res)} sample: {res}')
