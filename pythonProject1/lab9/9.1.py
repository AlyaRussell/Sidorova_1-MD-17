import os
from PIL import Image, ImageFilter

# Определяем имя исходной папки и папки, в которую будут сохранены обработанные изображения
im_dir = './images'
new_dir = './new_images'

# Проверяем, существует ли папка, куда будут сохранены обработанные изображения, и создаем ее при необходимости
if not os.path.exists(new_dir):
    os.mkdir(new_dir)

# Перебираем все файлы в папке с изображениями
for filename in os.listdir(im_dir):

    # Определяем полный путь к файлу
    filepath = os.path.join(im_dir, filename)

    # Проверяем, является ли файл изображением
    if not os.path.isfile(filepath) or not filename.lower().endswith('.jpg') and not filename.lower().endswith('.png'):
        continue  # Пропускаем файлы, которые не являются изображениями

    # Открываем изображение
    im = Image.open(filepath)

    # Применяем операцию к изображению
    im = im.filter(ImageFilter.BLUR)

    # Создаем имя для обработанного изображения и сохраняем его в новый файл
    new_filename = os.path.join(new_dir, filename)
    im.save(new_filename)

    print(f"Сохранено обработанное изображение: {new_filename}")