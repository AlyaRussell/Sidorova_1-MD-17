from PIL import Image

# Создаем словарь с парами "название праздника - имя файла с открыткой к нему"
holidays = {
    "Новый год": "new-year.jpg",
    "День рождения": "birthday.jpg",
    "День святого Валентина": "valentine.jpg",
    "8 Марта": "march-8.jpg"
}

# Запрашиваем у пользователя название праздника, для которого нужна открытка
holiday = input("Введите название праздника, для которого нужна открытка: ")

# Ищем имя файла с открыткой для выбранного праздника в словаре
if holiday in holidays:
    filename = holidays[holiday]

    # Открываем изображение и выводим его на экран
    img = Image.open(filename)
    img.show()

else:
    print("Открытка для этого праздника не найдена.")