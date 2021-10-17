
from PIL import Image, ImageFont, ImageDraw
from .pixel_type import PixelType
from os import getcwd
from utils import optional_environ


def new_inky_image(width=0, height=0):
    if width == 0:
        width = int(optional_environ('INKY_WIDTH', '400'))
    if height == 0:
        height = int(optional_environ('INKY_HEIGHT', '300'))
    img = Image.new("P", (width, height))
    return img


def set_pixel(image, point, color_type):
    image.putpixel(point, color_type.value)


def draw_text(image, text, size, point, color_type, anchor="la"):
    font_path = getcwd() + '/fonts/Roboto/Roboto-Regular.ttf'
    font = ImageFont.truetype(font_path, size)
    draw = ImageDraw.Draw(image)
    draw.text(
        xy=point,
        text=text,
        fill=color_type.value,
        font=font,
        anchor=anchor,
    )


def get_truncated_text(image, text, size, width):
    font_path = getcwd() + '/fonts/Roboto/Roboto-Regular.ttf'
    font = ImageFont.truetype(font_path, size)
    draw = ImageDraw.Draw(image)
    truncated = text
    if draw.textsize(text=truncated, font=font)[0] <= width:
        return truncated

    elipse_size = draw.textsize(text="...", font=font)[0]

    while True:
        size = draw.textsize(text=truncated, font=font)[0]
        if size <= (width - elipse_size):
            break
        if len(truncated) <= 0:
            break
        truncated = truncated[0:len(truncated) - 1]

    return truncated + "..."


def draw_rect(image, top_left, bottom_right, fill_color_type):
    draw = ImageDraw.Draw(image)
    draw.rectangle(
        xy=[top_left, bottom_right],
        fill=fill_color_type.value,
    )


def new_inky_draw(color='', mode=''):
    if len(color) == 0:
        color = optional_environ('INKY_COLOR', 'red')
    if len(mode) == 0:
        mode = optional_environ('INKY_MODE', 'inky')

    def inky_draw(image):
        if mode == 'demo':
            from .draw_demo import new_demo_draw
            drawer = new_demo_draw()
        else:
            from .draw_inky import new_inky_draw
            drawer = new_inky_draw(color)
        drawer(image)
    return inky_draw
