"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
_time = int(input("Enter time in seconds: "))
_time_hours = _time // 3600
_time_minutes = (_time - _time_hours * 3600) // 60
_time_seconds = _time - _time_hours * 3600 - _time_minutes * 60
print(f'Time: {_time_hours:>02}:{_time_minutes:>02}:{_time_seconds:>02}')
