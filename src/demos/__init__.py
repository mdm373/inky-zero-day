from inky_draw import PixelType, new_inky_image, set_pixel, new_inky_draw, write_text, write_rect
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
    image = new_inky_image(width, height)
    drawer = new_inky_draw(color, mode)
    write_rect(image, (0, 0), (image.width, 40), PixelType.COLOR)
    write_text(image, text, 22, (5, 5), PixelType.WHITE)

    write_text(image, text, 22, (5, 45), PixelType.BLACK)

    write_rect(image, (0, 80), (image.width, 120), PixelType.BLACK)
    write_text(image, text, 22, (5, 85), PixelType.WHITE)

    drawer(image)
