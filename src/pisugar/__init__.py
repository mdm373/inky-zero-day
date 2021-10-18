import math
from utils import install_path
from os.path import exists


def get_battery():
    file_name = f"{install_path()}/.temp/battery.txt"
    if not exists(file_name):
        return "err: no bat file"

    content = None
    with open(file_name) as f:
        content = f.readlines()
    if len(content) < 1:
        return "err: no bat content"

    parts = content[0].split()
    if len(parts) < 2:
        return "err: no bat parts"

    try:
        return f"{math.floor(float(parts[1]))}%"
    except Exception as e:
        print(f"bat error {e}")
        return "err: exception"
