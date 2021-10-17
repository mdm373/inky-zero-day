
from .read_image import new_read_image
from .palette import new_palette


def inky_draw(width, height, color, mode):
    if mode == 'demo':
        from .draw_demo import new_demo_draw
        pal, drawer = new_demo_draw()
    else:
        from .draw_inky import new_inky_draw
        pal, drawer = new_inky_draw(color)

    read = new_read_image(pal)
    image = read(width, height)
    drawer(image)
