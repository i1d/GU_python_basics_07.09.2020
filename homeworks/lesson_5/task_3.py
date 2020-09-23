"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""
f_name = "task_3.txt"
salary_limit = 20000
with open(f_name, "r") as f:
    rows = f.readlines()
#print(f'There are {len(rows)} rows in the "{f_name}" file. Here are some info about them:')
total_salary = 0
salary_cnt = 0
for num, row in enumerate(rows, 1):
    r = tuple(row.split())
    if len(r) >= 2:
        try:
            if int(r[1]) < salary_limit:
                print(f'This employee has salary < {salary_limit}: {r[0]}')
            total_salary += int(r[1])
            salary_cnt += 1
        except ValueError as err:
            print(f'Error. Check row #{num}. Seems salary format is not a number. Details: {err}')
print(f'Average salary = {total_salary / salary_cnt:.2f}')
