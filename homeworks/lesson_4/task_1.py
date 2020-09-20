"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys

s_arg = sys.argv

hours = rate = bonus = 0

try:
    hours = float(s_arg[1])
except ValueError:
    print("Hours parameter should be digit")
except IndexError:
    print("Wrong parameters qty. Must be 3.")

try:
    rate = float(s_arg[2])
except ValueError:
    print("Rate parameter should be digit")
except IndexError:
    print("Wrong parameters qty. Must be 3.")


try:
    bonus = float(s_arg[3])
except ValueError:
    print("Bonus parameter should be digit")
except IndexError:
    print("Wrong parameters qty. Must be 3.")

if len(s_arg) == 4 and (isinstance(hours, int) or isinstance(hours, float)) \
                    and (isinstance(rate, int) or isinstance(rate, float)) \
                    and (isinstance(bonus, int) or isinstance(bonus, float)):
    print(f'Salary = [({hours} * {rate}) + {bonus}] = {hours * rate + bonus:.2f}')
else:
    print("Wrong parameters.")
