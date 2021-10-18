from PIL import Image
import time


def new_inky_draw(color):
    from inky import InkyWHAT
    inky_display = InkyWHAT(color)

    def draw(image):
        inky_display.set_image(image)
        inky_display.show()
    return draw
