
def new_demo_draw():
    def draw(image):
        image.putpalette([255, 255, 255, 0, 0, 0, 125, 0, 0])
        image.show()
    return draw
