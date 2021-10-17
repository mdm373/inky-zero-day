import sys
import os


def optional_arg(index, default):
    arg_len = len(sys.argv)
    return default if arg_len <= index else sys.argv[index]


def optional_environ(name, default):
    return default if name not in os.environ else os.environ[name]
