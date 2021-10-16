from os import path
from PIL import Image
import time
from inky import InkyWHAT

def draw(requestPath):
    file_path = path.relpath(requestPath)
    inky_display = InkyWHAT('red')
    with open(file_path) as f:
        lines = f.readlines()
        print(lines)

    colours = (inky_display.RED, inky_display.BLACK, inky_display.WHITE)
    colour_names = (inky_display.colour, "black", "white")
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))

    # Loop through the specified number of cycles and completely
    # fill the display with each colour in turn.

    for i in range(3):
        print("Cleaning cycle %i\n" % (i + 1))
        for j, c in enumerate(colours):
            print("- updating with %s" % colour_names[j])
            inky_display.set_border(c)
            for x in range(inky_display.WIDTH):
                for y in range(inky_display.HEIGHT):
                    img.putpixel((x, y), c)
            inky_display.set_image(img)
            inky_display.show()
            time.sleep(1)
        print("\n")

    print("Cleaning complete!")