"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
val = int(input("Please enter positive integer value: "))
_max = val % 10
_val = val // 10
while _val > 0:
    if _val % 10 > _max:
        _max = _val % 10
    _val //= 10
print(f'Max digit in the value: {_max}')