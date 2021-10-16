from os import path

def draw(requestPath):
    file_path = path.relpath(requestPath)
    with open(file_path) as f:
        lines = f.readlines()
        print(lines)