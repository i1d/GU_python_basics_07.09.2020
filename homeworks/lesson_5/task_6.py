"""6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""


def get_val(_str):
    """converts "dirty" string to int"""

    _s = ""
    if _str == "—" or _str == "-":
        _s = 0
    else:
        for s in _str:
            if s.isnumeric():
                _s += s
    return int(_s)


f_in = "task_6_in.txt"
with open(f_in, "r") as f_in:
    d = {}
    h = 0
    for num, row in enumerate(f_in, 1):
        _r = []
        if len(row) > 1:  # "empty string has \n symbol"
            r = row.rstrip("\n").split(":")
            _r.append(r[0])
            r_ = r[1].lstrip(" ").rstrip(" ").split(" ")
            for i in r_:
                try:
                    _r.append(get_val(i))
                except ValueError as err:
                    print(f'There are something wrong with row #{num}. Details: {err}.')
            h = sum(_r[1:])
            d[_r[0]] = h
print(d)
