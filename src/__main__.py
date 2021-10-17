from inky_draw import inky_draw
from utils import get_optional_arg
from demo_writer import demo_writer

if __name__ == '__main__':
    def cmd_inky_draw():
        inky_draw(
            mode=get_optional_arg(2, 'inky'),
            width=int(get_optional_arg(3, 400)),
            height=int(get_optional_arg(4, 300)),
            color=get_optional_arg(5, 'red'),
        )

    def cmd_demo_writer():
        demo_writer(
            width=int(get_optional_arg(2, 400)),
            height=int(get_optional_arg(3, 300)),
        )
    commands = {
        'draw': cmd_inky_draw,
        'write': cmd_demo_writer,
    }
    commands[get_optional_arg(1, 'draw')]()
