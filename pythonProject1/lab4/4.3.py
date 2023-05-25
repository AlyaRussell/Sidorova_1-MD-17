def is_magic_date(date):
    # Разделение даты на компоненты
    day, month, year = map(int, date.split('.'))

    # Проверка на магическую дату
    if day * month == year % 100:
        return True
    else:
        return False