from utils import get_optional_arg
from demos import checker_demo, text_demo

if __name__ == '__main__':
    def cmd_checker_demo():
        checker_demo(
            mode=get_optional_arg(2, 'inky'),
            width=int(get_optional_arg(3, 400)),
            height=int(get_optional_arg(4, 300)),
            color=get_optional_arg(5, 'red'),
        )

    def cmd_text_demo():
        text_demo(
            text=get_optional_arg(2, 'hello'),
            mode=get_optional_arg(3, 'inky'),
            width=int(get_optional_arg(4, 400)),
            height=int(get_optional_arg(5, 300)),
            color=get_optional_arg(6, 'red'),
        )

    commands = {
        'checker': cmd_checker_demo,
        'text': cmd_text_demo,
    }
    commands[get_optional_arg(1, 'checker')]()
