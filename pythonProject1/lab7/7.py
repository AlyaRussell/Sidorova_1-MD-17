import os
from PIL import Image, ImageFilter
from getpass import getpass

filename = input("Введите имя файла: ")
im_1 = Image.open(filename)

im_1.show()

width, height = im_1.size
format = im_1.format
mode = im_1.mode

print(f"Ширина: {width}\nВысота: {height}\nФормат: {format}\nЦветовая модель: {mode}")

thumbnail_size = (int(im_1.width / 3), int(im_1.height / 3))
thumbnail_im = im_1.copy()
thumbnail_im.thumbnail(thumbnail_size)

im_dir = '../images'
if not os.path.exists(im_dir):
    os.mkdir(im_dir)
thumbnail_im.save(os.path.join(im_dir, 'thumbnail_' + filename))
im_1.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT).save(os.path.join(im_dir, 'horizontal_flip_' + filename))
im_1.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM).save(os.path.join(im_dir, 'vertical_flip_' + filename))

folder_path = input("Введите путь к папке: ")

files = [f for f in os.listdir(folder_path) if f.endswith('.jpeg')]

out_dir = '../output'
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

for file in files:
    original_im = Image.open(os.path.join(folder_path, file))
    filtered_im = original_im.filter(ImageFilter.MinFilter)
    filtered_im.save(os.path.join(out_dir, file))


parent_image_filename = input("Введите имя файла, на который нужно наложить водяной знак: ")
watermark_filename = input("Введите имя файла с водяным знаком: ")

parent_image = Image.open(parent_image_filename).load()
watermark = Image.open(watermark_filename).load()

watermark_size = (int(parent_image.width / 3), int(parent_image.height / 3))
watermark.thumbnail(watermark_size)

x = parent_image.width - watermark.width
y = parent_image.height - watermark.height

for i in range(watermark.width):
    for j in range(watermark.height):
        r, g, b, _ = watermark[i, j]
        if r < 155 and g < 155 and b < 155:
            parent_image[x + i, y + j] = (r, g, b)

parent_image.save(os.path.join(im_dir, 'watermarked_' + parent_image_filename))