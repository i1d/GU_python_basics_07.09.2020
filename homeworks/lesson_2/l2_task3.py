"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
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
if month in [12, 1, 2]:
    print(f'_list_: This month is in the "{seasons_list[0]}" season.')
elif month in [3, 4, 5]:
    print(f'_list_: This month is in the "{seasons_list[1]}" season.')
elif month in [6, 7, 8]:
    print(f'_list_: This month is in the "{seasons_list[2]}" season.')
elif month in [9, 10, 11]:
    print(f'_list_: This month is in the "{seasons_list[3]}" season.')
print(f'_dict_: This month is in the "{seasons_dict[month]}" season.')
