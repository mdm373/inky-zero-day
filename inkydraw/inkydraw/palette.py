from enum import Enum


class PixelType(Enum):
    BLACK = 'B'
    WHITE = 'W'
    COLOR = 'C'


def new_palette(black_val, white_val, color_val):
    return {
        PixelType.BLACK.value: black_val,
        PixelType.WHITE.value: white_val,
        PixelType.COLOR.value: color_val,
    }


def translate(palette, char):
    if char not in palette:
        raise Exception(f"invalid char {char} pixel type")
    return palette[char]
