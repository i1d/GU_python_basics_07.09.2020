"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""
r = 0


def list_sum(_list):
    """Returns sum of items in a list."""

    global r
    for item in _list:
        r += item
    return r


while True:
    s = input("Enter set of numbers divided with 'space' symbol. Special character for stop: ").split(" ")
    if not s[-1].isnumeric():
        _s = [float(val) for val in s[:-1]]
        print(list_sum(_s))
        break
    else:
        _s = [float(val) for val in s]
        print(list_sum(_s))

