def divide_100(number):
    try:
        result = 100 / number
        return result
    except ZeroDivisionError:
        print('Ошибка: делитель равен нулю')
    except ValueError:
        print('Ошибка: введено не число')

# Запрос числа у пользователя
user_input = input('Введите число: ')

# Вызов функции and работа с ошибками
try:
    number = int(user_input)
    print(divide_100(number))
except ValueError:
    print('Ошибка: введено не число')