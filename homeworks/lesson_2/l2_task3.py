"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
import datetime

while True:
    print("Enter number of month:", end=" ")
    month = input()
    if not month.isnumeric():
        print("Wrong input, month number must be a digit, try again.")
    elif 1 > int(month) or int(month) > 12:
        print("Wrong input, month number must be a digit between 1 and 12 inclusively, try again.")
    elif 1 <= int(month) <= 12:
        month = int(month)
        break
seasons_list = ["winter", "spring", "summer", "autumn"]
seasons_dict = {12: "winter", 1: "winter", 2: "winter",
                3: "spring", 4: "spring", 5: "spring",
                6: "summer", 7: "summer", 8: "summer",
                9: "autumn", 10: "autumn", 11: "autumn"}
t_1 = datetime.datetime.now()
if month in [12, 1, 2]:
    print(f'_list_: This month is in the "{seasons_list[0]}" season. ', end="")
elif month in [3, 4, 5]:
    print(f'_list_: This month is in the "{seasons_list[1]}" season. ', end="")
elif month in [6, 7, 8]:
    print(f'_list_: This month is in the "{seasons_list[2]}" season. ', end="")
elif month in [9, 10, 11]:
    print(f'_list_: This month is in the "{seasons_list[3]}" season. ', end="")
t_2 = datetime.datetime.now()
t_diff_list = t_2 - t_1
print(f'Time spent: {t_diff_list}')
t_1 = datetime.datetime.now()
print(f'_dict_: This month is in the "{seasons_dict[month]}" season. ', end="")
t_2 = datetime.datetime.now()
t_diff_dict = t_2 - t_1
print(f'Time spent: {t_diff_dict}')
print()
if t_diff_dict < t_diff_list:
    print(f'Conclusion: working with {type(seasons_dict)} is faster than working with {type(seasons_list)}: diff={t_diff_list - t_diff_dict}')
elif t_diff_dict > t_diff_list:
    print(f'Conclusion: working with {type(seasons_dict)} is slower than working with {type(seasons_list)}: diff={t_diff_dict - t_diff_list}')
else:
    print(f'Conclusion: working with {type(seasons_dict)} is equal working with {type(seasons_list)}: diff={t_diff_list - t_diff_dict}')
