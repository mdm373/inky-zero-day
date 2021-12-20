from utils import optional_arg
from commands import checker_demo, text_demo, calendar_demo
from calendar_client import save_calendar_tokens
from dotenv import load_dotenv
from auth_server import serve

if __name__ == '__main__':
    load_dotenv()

    def cmd_checker_demo():
        checker_demo()

    def cmd_text_demo():
        text_demo(optional_arg(2, 'Ohh, hi Mark.'))

    def cmd_get_tokens():
        save_calendar_tokens()

    def cmd_show_calendar():
        calendar_demo()

    def cmd_creds_server():
        serve()

    commands = {
        'checker': cmd_checker_demo,
        'text': cmd_text_demo,
        'tokens': cmd_get_tokens,
        'calendar': cmd_show_calendar,
        'serve': cmd_creds_server,
    }
    commands[optional_arg(1, 'text')]()
