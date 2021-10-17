import sys


def get_optional_arg(index, default):
    arg_len = len(sys.argv)
    return default if arg_len <= index else sys.argv[index]
