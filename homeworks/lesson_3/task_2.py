"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def enter_func(first_name="Ivan", last_name="Ivanov", year_of_birth=1900, city="Helsinki", email="ivan@ivanov.com", phone="+12345678900"):
    """Function to return set of named parameters of a user in a single row."""

    return f'{first_name} {last_name} ({year_of_birth}): {city}, {email}, {phone}'


print(enter_func(last_name='Fedorov', first_name='Petr', city="Tallinn", phone="+5134753634", year_of_birth=1950))

