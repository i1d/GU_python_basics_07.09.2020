"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""


def cnt(_cnt):
    return "s" if _cnt > 1 or _cnt == 0 else ""


f_name = "task_2.txt"
row_cnt = 0
with open(f_name, "r") as f:
    rows = f.readlines()
print(f'There are {len(rows)} rows in the "{f_name}" file. Here are some info about them:')
for num, row in enumerate(rows, 1):
    print(f'Row #{num}: ', end="")
    r = row.split()
    if len(r) > 0:
        i_c = 0
        w_c = 0
        for i in r:
            if i.isnumeric():
                i_c += 1
            else:
                w_c += 1
        print(f'There are {w_c} word{cnt(w_c)} in this row, and {i_c} number{cnt(i_c)}.')
    else:
        print(f'This is empty row.')
