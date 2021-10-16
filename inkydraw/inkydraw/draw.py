from .read_image import new_read_image
from .palette import new_palette


def draw(width, height, color, mode):
    if mode == 'demo':
        from .draw_demo import new_demo_draw
        palette, drawer = new_demo_draw()
    else:
        from .draw_inky import new_inky_draw
        palette, drawer = new_inky_draw(color)

    read_image = new_read_image(palette)
    image = read_image(width, height)
    drawer(image)
