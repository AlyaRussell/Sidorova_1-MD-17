from PIL import Image, ImageDraw, ImageFont

# Открываем изображение
img = Image.open("Открытка.jpg")

# Определяем размер изображения
width, height = img.size

# Получаем координаты области, которую нужно вырезать
left = int(input("Введите координату X левого верхнего угла области для выреза (от 0 до " + str(width) + "): "))
top = int(input("Введите координату Y левого верхнего угла области для выреза (от 0 до " + str(height) + "): "))
right = int(input("Введите координату X правого нижнего угла области для выреза (от " + str(left) + " до " + str(width) + "): "))
bottom = int(input("Введите координату Y правого нижнего угла области для выреза (от " + str(top) + " до " + str(height) + "): "))

# Обрезаем изображение
cropped_img = img.crop((left, top, right, bottom))

# Запрашиваем у пользователя имя, которое следует использовать в тексте
name = input("Введите имя, которое нужно использовать в тексте: ")

# Создаем объект ImageDraw и объект шрифта
draw = ImageDraw.Draw(cropped_img)
font = ImageFont.truetype("arialbd.ttf", 60)

# Форматируем текст и выводим его на изображение
text = "{} , поздравляю!".format(name)
text_color = (0, 0, 255)
text_width, text_height = font.getsize(text)
text_x = (cropped_img.width - text_width) / 2
text_y = cropped_img.height - text_height - 50
draw.text((text_x, text_y), text, font=font, fill=text_color)

# Сохраняем вырезанную область в новый файл в формате PNG
cropped_img.save("Открытка_cropped.png")