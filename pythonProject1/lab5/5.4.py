from random import randint
a = ["Сидорова", "Лыткин", "Гусев", "Тарнаева", "Иванов", "Назаренко", "Ившина", "Рахимов", "Васильев", "Жарко"]
b = ["Кашин", "Пугачева", "Лазарев", "Гагарина", "Басков", "Леонтьев", "Бузова", "Билан", "Агутин", "Воробьев"]
c = []*10
k=0
tmp = 0
cnt = 0
while tmp < 10:
    if tmp < 5:
        ch = randint(0, 9)
        if a[ch] in c:
           k += 1
        else:
            c.append(a[ch])
            tmp += 1
    elif tmp <10:
        ch = randint(0, 9)
        if b[ch] in c:
            k += 1
        else:
            c.append(b[ch])
            tmp += 1
if "Жарко" in c:
    cnt += 1
c = tuple(sorted(c))
print(a)
print(b)
print(c, len(c))
print("Людей с фамилией Жарко в команде: ", cnt)