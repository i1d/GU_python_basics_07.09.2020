"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""
import datetime

while True:
    print("Enter a sentence using the 'space' symbol as a words delimiter:")
    sentence = input()
    if " " not in sentence:
        print("Space is absent, try again.")
    elif len(sentence.split()) <= 1:
        print("Enter at least 2 words (or more). Try again.")
    else:
        sentence = sentence.split()
        break

run_count_no_enum = 0
run_count_enum = 0
while True:
    while True:
        print("Choose solution (1 - with no enumerator; 2 - with enumerator):")
        option = input()
        if not option.isnumeric():
            print("Wrong input, option must be a digit: 1 or 2.")
        elif int(option) not in [1, 2]:
            print("Wrong input, option must be 1 or 2.")
        else:
            option = int(option)
            break
    if option == 1:
        t_1 = datetime.datetime.now()
        i = 0
        for word in sentence:
            print(f'Row #{i}: {word[0:10]}')
            i += 1
        t_2 = datetime.datetime.now()
        t_diff_no_enum = t_2 - t_1
        print(f'\nTime spent: {t_diff_no_enum}\n')
        run_count_no_enum += 1
    elif option == 2:
        t_1 = datetime.datetime.now()
        for row, word in enumerate(sentence, 1):
            print(f'Row #{row}: {word[0:10]}')
        t_2 = datetime.datetime.now()
        t_diff_enum = t_2 - t_1
        print(f'\nTime spent: {t_diff_enum}\n')
        run_count_enum += 1
    print("Would you like to try another option (y/n)?")
    while True:
        opt = input()
        if opt not in ("y", "n"):
            print("Choose 'y' or 'n'")
        else:
            break
    if opt == "n":
        break

if run_count_no_enum >= 1 and run_count_enum:
    if t_diff_no_enum < t_diff_enum:
        print(f'Conclusion: working with "no enumerator" is faster than working with "enumerator": diff={t_diff_enum - t_diff_no_enum}')
    elif t_diff_no_enum > t_diff_enum:
        print(f'Conclusion: working with "no enumerator" is slower than working with "enumerator: diff={t_diff_no_enum - t_diff_enum}')
    else:
        print(f'Conclusion: working with "no enumerator" is equal working with "enumerator": diff={t_diff_no_enum - t_diff_enum}')
