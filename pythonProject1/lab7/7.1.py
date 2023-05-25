from PIL import Image

# Открытие изображения
image = Image.open('башня.jpeg')

# Информация о размере изображения
width, height = image.size
print(f'Размер изображения: {width} x {height}')

# Информация о формате файла
print(f'Формат файла: {image.format}')

# Информация о цветовой модели
print(f'Цветовая модель: {image.mode}')

# Отображение изображения
image.show()
