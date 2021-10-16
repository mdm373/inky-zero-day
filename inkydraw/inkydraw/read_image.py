import sys
from .palette import translate, new_palette
from PIL import Image


def new_read_image(palette):
    def read_image(width, height):
        raw_image = sys.stdin.readline().rstrip()
        if len(raw_image) != width * height:
            raise Exception(f"invalid raw image len {len(raw_image)}, expected {height * width} for {width}X{height}")

        img = Image.new("P", (width, height))
        index = -1
        for char in raw_image:
            index = index + 1
            x = index % width
            y = index // width
            val = translate(palette, char)
            img.putpixel((x, y), val)
        return img
    return read_image
