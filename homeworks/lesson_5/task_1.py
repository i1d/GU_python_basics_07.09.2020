"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""
f_name = "task_1.txt"
print("Enter data to input them to the file. Hit Enter when finish.")
with open(f_name, "w") as f:
    while True:
        s = input()
        if len(s) == 0:
            break
        else:
            print(s, file=f)
print("Thank you. You have entered:")
with open(f_name, "r") as f:
    for line in f:
        print(line, end="")
print("Bye.")
