"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(_str):
    """Returns word with first capital letter"""

    return _str[0].upper() + _str[1:]

def int_func_2(_str):
    """Returns word with first capital letter without using of upper() function."""

    alphabet_lower = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    alphabet_upper = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    return alphabet_upper[alphabet_lower.index(_str[0])] + _str[1:] if _str[0] in alphabet_lower else _str


print(int_func_2("text"))

sentence = input("Enter set of words divided with 'space' symbol:\n").split(" ")
print(" ".join([int_func(word) for word in sentence]))
