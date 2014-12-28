from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def write_number(image_file_path, number=1):
    img = Image.open(image_file_path)
    font_size = img.size[0] if img.size[0] < img.size[1] else img.size[1]
    font_size = font_size / 4
    number_txt = str(number) + ' ' if number < 100 else '99+'
    font = ImageFont.truetype("arial.ttf", size=font_size)
    if font.getsize(number_txt)[0] > img.size[0] or font.getsize(number_txt)[1] > img.size[1]:
        return img
    position = img.size[0] - font.getsize(number_txt)[0]
    ImageDraw.Draw(img).text((position, 0), number_txt, (255, 0, 0), font)
    return img

write_number('resource/1.bmp').save('result.png')
#write_number('resource/1.bmg', 100).save('result100.png')