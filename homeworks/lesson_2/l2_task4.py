"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""
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
    i = 0
    for word in sentence:
        print(f'Row #{i}: {word[0:10]}')
        i += 1
elif option == 2:
    for row, word in enumerate(sentence, 1):
        print(f'Row #{row}: {word[0:10]}')

