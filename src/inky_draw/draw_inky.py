from PIL import Image
import time


def new_inky_draw(color):
    from inky import InkyWHAT
    inky_display = InkyWHAT(color)

    def draw(image):
        inky_display.set_image(image)
        inky_display.show()
    return draw


def clear():
    from inky import InkyWHAT

    inky_display = InkyWHAT('red')
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
