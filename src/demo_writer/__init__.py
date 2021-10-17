

def demo_writer(width, height):
    to_write = ""
    values = ['B', 'W', 'C']

    index = 0
    for y in range(0, height):
        for x in range(0, width):
            index = index + 1
            if index >= len(values):
                index = 0
            to_write = to_write + values[index]
    print(to_write)
