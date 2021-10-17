from .palette import new_palette


def new_demo_draw():
    palette = new_palette(0, 1, 2)  # todo parameterize color properly

    def draw(image):
        image.putpalette([255, 255, 255, 0, 0, 0, 255, 0, 0])
        image.show()

    return palette, draw
