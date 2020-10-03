"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""
int_digits = list(map(str, (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)))


class NumberError(Exception):
    def __init__(self, text):
        self.text = text


def is_int(str):
    """Check if string can be converted to int"""
    c = 0
    for el in str:
        if el in int_digits:
            c += 1
    if c == len(str):
        return True
    else:
        return False


def is_float(str):
    """Check if string can be converted to float"""
    c = 0
    cd = 0
    for el in str:
        if el == ".":
            cd += 1
    if cd > 1 or (cd == 1 and len(str) == 1):
        return False
    else:
        idx = str.find(".")
        n_str = str[0:idx] + str[idx + 1:]
        for el in n_str:  # нужно снова проверить каждый элемент, тк какой-то может оказаться не цифрой
            if is_int(el):
                c += 1
        if c == len(n_str):
            return True
        else:
            return False


inp = ""
lst = []
while True:
    inp = input(f"\nEnter a number to add it to the list {lst}: ")
    try:
        if is_int(inp):
            lst.append(int(inp))
   #         print(f"Our list: {lst}.")
        elif is_float(inp):  # чтоб в массиве могли оказаться числа как int, так и float
            lst.append(float(inp))
    #        print(f"Our list: {lst}.")
        elif inp.lower() == "stop":
            print(f"Our final list: {lst}.\nThank you, bye.")
            break
        else:
            raise NumberError(f"This is not a number. This is {type(inp)}.")
    except NumberError as err:
        print(f"{err} Our list: {lst}.")
