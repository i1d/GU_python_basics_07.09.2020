"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
revenue = int(input("Enter revenue: "))
loss = int(input("Enter loss: "))
if revenue > loss:
    print("Profit! :)")
    profitability = revenue / loss
    employees_qty = int(input("Enter employees quantity: "))
    print(f'Profitability factor: {profitability:.2f}')
    print(f'Income by employee: {(revenue - loss) / employees_qty:.2f}')
elif revenue == loss:
    print("Zero :/")
elif revenue < loss:
    print("Loss :(")
