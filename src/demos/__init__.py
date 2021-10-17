from inky_draw import PixelType, new_inky_image, set_pixel, new_inky_draw
from PIL import ImageDraw, ImageFont
from os import getcwd


def checker_demo(mode, width, height, color):
    values = [PixelType.BLACK, PixelType.WHITE, PixelType.COLOR]
    image = new_inky_image(width, height)
    drawer = new_inky_draw(color, mode)
    index = 0
    for y in range(0, height):
        for x in range(0, width):
            index = index + 1
            if index >= len(values):
                index = 0
            set_pixel(image, (x, y), values[index])

    drawer(image)


def text_demo(mode, width, height, color, text):
    path = getcwd() + '/fonts/Roboto/Roboto-Regular.ttf'
    print(path)
    font = ImageFont.truetype(
        path, 20,
    )
    image = new_inky_image(width, height)
    drawer = new_inky_draw(color, mode)
    draw = ImageDraw.Draw(image)
    draw.text(
        xy=(5, 5),
        text=text,
        fill=PixelType.BLACK.value,
        font=font,

    )
    drawer(image)
