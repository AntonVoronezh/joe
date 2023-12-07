from PIL import Image, ImageDraw, ImageFont

from get_path import result_tmp_path
from helpers.shared.get_today import get_today


def get_image(path_out):
    im = Image.open(f'{result_tmp_path}/img.png')

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("trebuc.ttf", size=20)
    shape = [(0, 0), (150, 50)]
    draw.rectangle(shape, fill='#000000')
    today = f'{get_today()}'
    draw.text((20, 10), today, '#cccccc', font)

    im.save(f'{path_out}.png', quality=75)

