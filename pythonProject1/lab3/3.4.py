import random

correct_answers = 0  # количество правильных ответов
wrong_answers = 0  # количество неправильных ответов

while wrong_answers < 3:
    # Генерация двух случайных чисел
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    # Вывод выражения для решения
    answer = input(f'{a} + {b} = ')

    # Проверка ответа
    if int(answer) == a + b:
        print('Правильно!')
        correct_answers += 1
    else:
        print('Ответ неверный')
        wrong_answers += 1

# Вывод результата
print(f'Игра окончена. Правильных ответов: {correct_answers}')