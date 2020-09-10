"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
a = int(input("Enter distance in km for 1st day: "))
b = int(input("Enter target distance in km: "))
if b < a:
    print("Target distance should be >= distance for 1st day.")
else:
    d = 1
    while a <= b:
        print(f'Day {d}: {a:.2f} km')
        a *= 1.1
        d += 1
    print(f'Day {d}: {a:.2f} km')
    print(f'It will take {d} days to reach target distance.')
