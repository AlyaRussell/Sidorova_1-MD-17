e = int(input("Введите интересующий Вас год:  "))
if (e % 4 == 0) and (e % 100 != 0) or (e % 400 == 0):
    print("это високосный год")
else:
    print("это НЕ високосный год")