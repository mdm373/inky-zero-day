from .draw import draw as _draw
import sys


def get_optional_arg(index, default):
    arg_len = len(sys.argv)
    return default if arg_len <= index else sys.argv[index]


def draw():
    _draw(
        width=int(get_optional_arg(1, 400)),
        height=int(get_optional_arg(2, 300)),
        color=get_optional_arg(3, 'red'),
        mode=get_optional_arg(4, 'inky'),
    )
