import os
from PIL import Image, ImageFilter

filename = input("Введите имя файла: ")
im_1 = Image.open(filename)

file_root, file_ext = os.path.splitext(filename)

im_dir = '../images'
if not os.path.exists(im_dir):
    os.mkdir(im_dir)

im_1.save(os.path.join(im_dir, file_root + '_original' + file_ext))

for method in [ImageFilter.MinFilter, ImageFilter.BLUR, ImageFilter.SHARPEN]:
    new_image = im_1.filter(method)
    new_filename = os.path.join(im_dir, file_root + '_' + method.__name__ + file_ext)
    new_image.save(new_filename)
    print(f"Сохранено обработанное изображение: {new_filename}")