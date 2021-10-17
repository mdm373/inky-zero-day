
from PIL import Image
from .pixel_type import PixelType


def new_inky_image(width, height):
    img = Image.new("P", (width, height))
    return img


def set_pixel(image, point, pixel):
    image.putpixel(point, pixel.value)


def new_inky_draw(color, mode):
    def inky_draw(image):
        if mode == 'demo':
            from .draw_demo import new_demo_draw
            drawer = new_demo_draw()
        else:
            from .draw_inky import new_inky_draw
            drawer = new_inky_draw(color)
        drawer(image)
    return inky_draw
