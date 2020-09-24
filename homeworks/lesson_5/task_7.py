"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""
import json

lst = ["ООО", "OOO", "ИП", "ОАО", "ЗАО"]

f_in = "task_7_in.txt"
with open(f_in, "r") as f_in:
    d_firms = {}
    d_average_profit = {}
    sum_profit = 0
    profit_count = 0
    for num, row in enumerate(f_in, 1):
        _r = []
        pos = 0
        if len(row) > 1:  # "empty string has \n symbol"
            r = row.rstrip("\n").split(" ")
            for i in r:
                if i in lst:
                    pos = r.index(i)
                    r_comp_name = " ".join(r[0:pos])
                    income = float(r[pos + 1])
                    expense = float(r[pos + 2])
                    profit = round(income - expense, 2)
                    if profit > 0:
                        print(f'"{r_comp_name}" profit is: {profit:.2f}')
                        sum_profit += profit
                        profit_count += 1
                    average_profit = round(sum_profit / profit_count, 2)
                    d_firms[r_comp_name] = profit
                    d_average_profit["average_profit"] = average_profit
            if pos == 0:
                print(f"Company organization form is not found in row #{num}.")
    print(f'Average profit is: {average_profit}\n')

    l = [d_firms, d_average_profit]
    print(l)

with open("task_7_out.json", "w", encoding="UTF-8") as f_json_out:
    json.dump(l, f_json_out, ensure_ascii=False)
